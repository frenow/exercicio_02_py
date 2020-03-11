from django.db import models

class Endereco(models.Model):
    logradouro = models.CharField(max_length=60)
    numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=15)
    cidade = models.CharField(max_length=60)
    uf = models.CharField(max_length=2)
