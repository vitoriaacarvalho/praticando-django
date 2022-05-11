from unittest.util import _MAX_LENGTH
from django.db import models

class Cliente(models.Model):
    nome=models.CharField(max_length=25)
    idade=models.IntegerField()
    endereco=models.CharField(max_length=150)

def __str__(self):
    return self.name

class Pet(models.Model):
    nome=models.CharField(max_length=25)
    idade=models.IntegerField()
    breed=models.CharField(max_length=30)
    color=models.CharField(max_length=30)

def __str__(self):
    return self.name

# Create your models here.
