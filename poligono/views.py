from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


# Create your views here.
