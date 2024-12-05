from django.db import models
from datetime import date, datetime

# Create your models here.

# Nome do produto (String, obrigatório).
# Código do produto (String, único, obrigatório).
# Descrição (Texto longo, opcional).
# Preço (Decimal com 2 casas decimais).
# Quantidade em estoque (Número inteiro).
# Data de criação (Registrada automaticamente).


class Produto(models.Model):
    nome = models.CharField(max_length=150, blank=False)
    codproduto = models.CharField(max_length=150, unique=True, blank=False)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    data_de_criacao = models.DateTimeField(datetime.now(), editable=True)
    atualizado_em = models.DateTimeField(auto_now=True)
