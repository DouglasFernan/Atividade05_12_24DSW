from django.contrib import admin
from core.models import Produto

# Register your models here.

# Em seguida, registre o modelo na aplicação admin do django com as seguintes configurações:
# Exiba na listagem os campos código, nome, preço, quantidade em estoque e data de criação;
# Permita a busca do produto via código ou nome;
# Permita a filtragem de dados via data de criação;
# Ordene os itens por data de criação decrescente.


class ProdutoAdmin(admin.ModelAdmin):
    fields = ('nome', 'preco', 'quantidade', 'codproduto', 'data_de_criacao')
    exclude = ('descricao',)
    list_display = ('codproduto', 'nome', 'preco', 'quantidade', 'data_de_criacao')
    search_fields = ('codproduto', 'nome')
    list_filter = ('data_de_criacao',)
    ordering = ('-data_de_criacao',)


admin.site.register(Produto, ProdutoAdmin)
