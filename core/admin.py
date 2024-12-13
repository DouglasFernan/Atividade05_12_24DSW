from django.contrib import admin
from core.models import Produto, Fornecedor, Categoria

class ProdutoAdmin(admin.ModelAdmin):
    fields = ('nome', 'preco', 'quantidade', 'codproduto', 'data_de_criacao', 'fornecedor', 'categoria')
    exclude = ('descricao',)
    list_display = ('codproduto', 'nome', 'preco', 'quantidade', 'data_de_criacao', 'fornecedor', 'get_categorias')
    search_fields = ('codproduto', 'nome', 'fornecedor__name', 'categoria__name')
    list_filter = ('data_de_criacao', 'fornecedor', 'categoria')
    ordering = ('-data_de_criacao',)
    autocomplete_fields = ('fornecedor', 'categoria')

    def get_categorias(self, obj):
        return ", ".join([categoria.name for categoria in obj.categoria.all()])

    get_categorias.short_description = "Categorias"

admin.site.register(Produto, ProdutoAdmin)

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('name', 'empresa', 'email')  
    search_fields = ('name', 'empresa', 'email') 
    list_filter = ('empresa',)  

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',) 
