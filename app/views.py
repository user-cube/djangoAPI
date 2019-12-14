from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
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
        print("Sem token")
        token = ""
    return token

def isSuperUser(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        print(decoded)
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
        print(decoded)
        user = decoded['username']
    except:
        print("Erro no token")
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
        print("Erro no token")
    try:
        encomendas = Encomenda.objects.filter(user=user)
    except Encomenda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EncomendaSerializer(encomendas, many=True)
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
        return Response(status=status.HTTP_404_NOT_FOUND)

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
        return Response(status=status.HTTP_404_NOT_FOUND)
