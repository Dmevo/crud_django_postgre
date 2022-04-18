from django.db import models

# Create your models here.

class Produto(models.Model):
     
    nome = models.CharField(max_length=20)

    descricao = models.CharField(max_length=100)

    preco = models.IntegerField()
