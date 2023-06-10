from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Categoria, Producto
from django.contrib.auth.hashers import make_password
from django.db import models

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8)

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password')
    def validate_password(self, value):
        return make_password(value)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        #fields = ('nombre', 'descripcion')

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = '__all__'
        #fields = ('codigodeBarras',"nombre" ,'descripcion','peso','precio','cantidad')


