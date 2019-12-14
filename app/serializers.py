from app.models import Items, Profile, Encomenda
from rest_framework import serializers
from django.contrib.auth.models import User


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('id', 'titulo', 'picture', 'descricao', 'short', 'preco')


class EncomendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encomenda
        fields = ('data', 'produtos', 'user', 'quantidade', 'preco', 'total')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('nome', 'user', 'picture', 'morada', 'zipcode', 'pais')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'