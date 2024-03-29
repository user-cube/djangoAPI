from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers import *
from djangoAPI.settings import SECRET_KEY
import jwt

# Create your views here.

def getToken(request):
    """
    Get token from headers.
    """
    try:
        token = request.META['HTTP_AUTHORIZATION'].split()[1]
    except:
        token = ""
    return token

def isValid(token):
    """
    Check if token is valid.
    """
    try:
        decoded = jwt.decode(token, SECRET_KEY)
        return True
    except:
        return False

def isSuperUser(token):
    """
    Check if user is super user.
    """
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        if decoded['is_superuser'] == True:
            return True
    except:
        return False

@api_view(['GET'])
def get_items(request):
    """
    Obtém todos os items disponíveis.
    """
    items = Items.objects.all()
    serializer = ItemsSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_items_by_name(request, name):
    """
    Pesquisa de items por nome.
    """
    try:
        items = Items.objects.filter(titulo__icontains=name)
    except Items.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ItemsSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_items_info(request, id):
    """
    Informações de um produto.
    """
    try:
        items = Items.objects.filter(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ItemsSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_user(request):
    """
    Informações de perfil do utilizador.
    """
    user = ""
    token = getToken(request)
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user = decoded['username']
    except:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)


@api_view(['GET'])
def get_user_encomendas(request):
    """
    Lista de compras do utilizador.
    """
    user = ""
    token = getToken(request)
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user = decoded['username']
    except:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    try:
        encomendas = Encomenda.objects.filter(user=user).order_by("-id")
    except Encomenda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EncomendaReadSerializer(encomendas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_admin_panel(request):
    """
    Painel de administrador.
    """
    token = getToken(request)
    superUser = isSuperUser(token)

    if superUser == True:
        try:
            items = Items.objects.all()
        except Items.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ItemsSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['DELETE'])
def deleteItems(request, id):
    """
    Delete Item
    """
    token = getToken(request)
    superUser = isSuperUser(token)

    if superUser == True:
        try:
            items = Items.objects.get(id=id)
        except Items.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_encomendas_admin(request):
    """
    Obtém todas as encomendas realizadas na loja.
    """
    token = getToken(request)
    superUser = isSuperUser(token)

    if superUser == True:
        try:
            encomendas = Encomenda.objects.all().order_by("-id")
        except Encomenda.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EncomendaReadSerializer(encomendas, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def search_encomendas_admin(request, name):
    """
    Pesquisar encomedas realizadas na loja.
    """
    token = getToken(request)
    superUser = isSuperUser(token)

    if superUser == True:
        try:
            encomendas = Encomenda.objects.filter(produtos__titulo__contains=name).order_by("-id")
        except Encomenda.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EncomendaReadSerializer(encomendas, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def search_encomendas(request, name):
    """
    Pesquisar encomendas do utilizador.
    """
    token = getToken(request)
    if isValid(token):
        try:
            encomendas = Encomenda.objects.filter(produtos__titulo__contains=name).order_by("-id")
        except Encomenda.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EncomendaReadSerializer(encomendas, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT'])
def edit_perfil(request):
    """
    Alteração do perfil individual.
    """
    user = request.data['user']
    token = getToken(request)
    if isValid(token):
        try:
            user = Profile.objects.get(user=user)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT'])
def edit_items(request):
    """
    Permite editar os items existentes na base de dados.
    """
    token = getToken(request)
    superUser = isSuperUser(token)
    if superUser == True:
        id = request.data['id']
        try:
            items = Items.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ItemsSerializer(items, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def add_items(request):
    """
    Adicionar items à loja.
    """
    token = getToken(request)
    if isValid(token):
        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = ProfileSerializer (data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_encomenda(request):
    token = getToken(request)
    if isValid(token):
        serializer = EncomendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)