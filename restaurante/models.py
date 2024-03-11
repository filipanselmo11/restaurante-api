from django.db import models

# Create your models here.

class Restaurante(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)