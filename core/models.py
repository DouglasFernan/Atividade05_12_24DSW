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
    name = models.CharField("nome", max_length=150)
    empresa = models.CharField("nome da empresa", max_length=100)
    email = models.EmailField("email", max_length=254, unique=True)
    description = models.TextField("descrição", blank=True)

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        return self.name


class Categoria(models.Model):
    name = models.CharField("nome", max_length=100)
    description = models.TextField("descrição", blank=True)

    def __str__(self):
        return self.name


class Produto(models.Model):
    nome = models.CharField(max_length=150, blank=False)
    codproduto = models.CharField(max_length=150, unique=True, blank=False)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    data_de_criacao = models.DateTimeField(
        default=datetime.now, editable=True)  # Ajustado aqui
    atualizado_em = models.DateTimeField(auto_now=True)
    fornecedor = models.ForeignKey(
        'Fornecedor', verbose_name=("Fornecedor"), on_delete=models.CASCADE)
    categoria = models.ManyToManyField('Categoria', verbose_name=("Categoria"))

    def __str__(self):
        return self.nome
