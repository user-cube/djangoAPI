from app.models import Items, Profile, Wishlist, Encomenda
from rest_framework import serializers


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
