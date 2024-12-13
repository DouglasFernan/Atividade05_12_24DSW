from django.shortcuts import render
from . import models
from django.views.generic import FormView, ListView, UpdateView
from django.urls import reverse_lazy

# Create your views here.


class CoreListView(ListView):
    model = models.Produto


class ProdutoUpdate(UpdateView):
    model = models.Produto
    fields = ['nome', 'preco', 'quantidade', 'codproduto', 'descricao']
    success_url = reverse_lazy('listar_produtos')
