from django import forms
from django.forms import ModelForm
from .models import Produto, Fornecedor, Categoria


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'codproduto', 'descricao',
                  'preco', 'quantidade', 'fornecedor', 'categoria']


class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['name', 'empresa', 'email',
                  'description']


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['name', 'description']
