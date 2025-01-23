from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.CoreListView.as_view(), name="listar_produtos"),
    path("edit/<int:pk>/",  views.ProdutoUpdate.as_view(), name='editar_produtos'),
    path('criar_produto/', views.ProdutoCreate.as_view(), name='create'),
    path('criar_fornecedor/', views.FornecedorCreate.as_view(), name='create_fornecedor'),
    path('criar_categoria/', views.CategoriaCreate.as_view(), name='create_categoria'),

]

# produto form

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     <form method="post">{% csrf_token %}
#         {{ form.as_p }}
#     <input type="submit" value="Salvar" />
#     </form>

# </body>
# </html>

# produto list

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     <h1>Produtos</h1>
#     <ul>
#         {% for produto in object_list %}
#             <li>{{ produto.nome }}  :
#             <a href="{% url "editar_produtos" produto.pk %}">editar</a>
#             </li>
#         {% endfor %}
#     </ul>
#     <a href="">New</a>
# </body>
# </html>

# views

# from django.shortcuts import render
# from . import models
# from django.views.generic import FormView, ListView, UpdateView
# from django.urls import reverse_lazy

# # Create your views here.


# class CoreListView(ListView):
#     model = models.Produto


# class ProdutoUpdate(UpdateView):
#     model = models.Produto
#     fields = ['nome', 'preco', 'quantidade', 'codproduto', 'descricao']
#     success_url = reverse_lazy('listar_produtos')

# admin

# from django.contrib import admin
# from core.models import Produto, Fornecedor, Categoria

# class ProdutoAdmin(admin.ModelAdmin):
#     fields = ('nome', 'preco', 'quantidade', 'codproduto', 'data_de_criacao', 'fornecedor', 'categoria')
#     exclude = ('descricao',)
#     list_display = ('codproduto', 'nome', 'preco', 'quantidade', 'data_de_criacao', 'fornecedor', 'get_categorias')
#     search_fields = ('codproduto', 'nome', 'fornecedor__name', 'categoria__name')
#     list_filter = ('data_de_criacao', 'fornecedor', 'categoria')
#     ordering = ('-data_de_criacao',)
#     autocomplete_fields = ('fornecedor', 'categoria')

#     def get_categorias(self, obj):
#         return ", ".join([categoria.name for categoria in obj.categoria.all()])

#     get_categorias.short_description = "Categorias"

# admin.site.register(Produto, ProdutoAdmin)

# @admin.register(Fornecedor)
# class FornecedorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'empresa', 'email')
#     search_fields = ('name', 'empresa', 'email')
#     list_filter = ('empresa',)

# @admin.register(Categoria)
# class CategoriaAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)


# models
# from django.db import models
# from datetime import date, datetime

# # Create your models here.

# # Nome do produto (String, obrigatório).
# # Código do produto (String, único, obrigatório).
# # Descrição (Texto longo, opcional).
# # Preço (Decimal com 2 casas decimais).
# # Quantidade em estoque (Número inteiro).
# # Data de criação (Registrada automaticamente).


# class Fornecedor(models.Model):
#     name = models.CharField("name", max_length=150)
#     empresa = models.CharField("company name", max_length=100)
#     email = models.EmailField("email", max_length=254, unique=True)
#     description = models.TextField("description", blank=True)

#     class Meta:
#         verbose_name = "Fornecedor"
#         verbose_name_plural = "Fornecedores"

#     def __str__(self):
#         return self.name


# class Categoria(models.Model):
#     name = models.CharField("name", max_length=100)
#     description = models.TextField("description", blank=True)

#     def __str__(self):
#         return self.name


# class Produto(models.Model):
#     nome = models.CharField(max_length=150, blank=False)
#     codproduto = models.CharField(max_length=150, unique=True, blank=False)
#     descricao = models.TextField()
#     preco = models.DecimalField(max_digits=10, decimal_places=2)
#     quantidade = models.IntegerField()
#     data_de_criacao = models.DateTimeField(datetime.now(), editable=True)
#     atualizado_em = models.DateTimeField(auto_now=True)
#     fornecedor = models.ForeignKey(
#         Fornecedor, verbose_name=(""), on_delete=models.CASCADE)
#     categoria = models.ManyToManyField(Categoria,  verbose_name=(""))
