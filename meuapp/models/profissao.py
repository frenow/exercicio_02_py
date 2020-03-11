from django.db import models

class Profissao(models.Model):
    descricao = models.CharField(max_length=60)