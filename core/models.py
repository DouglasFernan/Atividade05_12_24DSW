from django.db import models
from datetime import date, datetime

# Create your models here.

# Nome do produto (String, obrigatório).
# Código do produto (String, único, obrigatório).
# Descrição (Texto longo, opcional).
# Preço (Decimal com 2 casas decimais).
# Quantidade em estoque (Número inteiro).
# Data de criação (Registrada automaticamente).


class Fornecedor(models.Model):
    name = models.CharField("name", max_length=150)
    empresa = models.CharField("company name", max_length=100)
    email = models.EmailField("email", max_length=254, unique=True)
    description = models.TextField("description", blank=True)

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        return self.name


class Categoria(models.Model):
    name = models.CharField("name", max_length=100)
    description = models.TextField("description", blank=True)

    def __str__(self):
        return self.name


class Produto(models.Model):
    nome = models.CharField(max_length=150, blank=False)
    codproduto = models.CharField(max_length=150, unique=True, blank=False)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    data_de_criacao = models.DateTimeField(datetime.now(), editable=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    fornecedor = models.ForeignKey(
        Fornecedor, verbose_name=(""), on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria,  verbose_name=(""))
