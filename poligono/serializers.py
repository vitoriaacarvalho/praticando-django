from rest_framework import serializers
from .models import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'idade', 'endereco']



class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['nome', 'idade', 'breed', 'color']

