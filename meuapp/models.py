from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    idade = models.IntegerField(null=True)
    data_nacimento = models.DateField(null=True)

class Endereco(models.Model):
    logradouro = models.CharField(max_length=60)
    numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=15)
    cidade = models.CharField(max_length=60)
    uf = models.CharField(max_length=2)

class Profissao(models.Model):
    descricao = models.CharField(max_length=60)

