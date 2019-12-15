from app.models import Items, Profile, Encomenda
from rest_framework import serializers
from django.contrib.auth.models import User


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'


class EncomendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encomenda
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'