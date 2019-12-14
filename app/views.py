from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers import *


# Create your views here.

@api_view(['GET'])
def get_items(request):
    items = Items.objects.all()
    serializer = ItemsSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_items_by_name(request, name):
    try:
        items = Items.objects.filter(titulo__icontains=name)
    except Items.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ItemsSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_user(request):
    username = request.GET['user']
    try:
        profile = Profile.objects.get(user=username)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)


@api_view(['GET'])
def get_user_encomendas(request):
    user = request.GET['user']
    try:
        encomendas = Encomenda.objects.filter(user=user)
    except Encomenda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EncomendaSerializer(encomendas, many=True)
    return Response(serializer.data)