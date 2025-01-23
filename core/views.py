from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from . import models
from django.views.generic import FormView, ListView, UpdateView, CreateView
from django.urls import reverse, reverse_lazy
from .forms import ProdutoForm, FornecedorForm, CategoriaForm
from django import forms
# Create your views here.


class CoreListView(ListView):
    model = models.Produto


class ProdutoUpdate(UpdateView):
    model = models.Produto
    fields = ['nome', 'preco', 'quantidade', 'codproduto', 'descricao']
    success_url = reverse_lazy('listar_produtos')


class ProdutoCreate(CreateView):
    model = models.Produto
    form_class = ProdutoForm
    template_name = "core/create.html"
    success_url = reverse_lazy("listar_produtos")


class FornecedorCreate(CreateView):
    model = models.Fornecedor
    form_class = FornecedorForm
    template_name = "core/create_fornecedor.html"
    success_url = reverse_lazy("listar_produtos")


class CategoriaCreate(CreateView):
    model = models.Categoria
    form_class = CategoriaForm
    template_name = "core/create_categoria.html"
    success_url = reverse_lazy("listar_produtos")
