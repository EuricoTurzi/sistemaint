from django.contrib import admin
from .models import CadastroTipoProduto, EntradaProduto

# Register your models here.

@admin.register(CadastroTipoProduto)
class CadastroTipoProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome_produto', 'fabricante', 'valor_unitario', 'data_cadastro']
    list_filter = ['fabricante', 'data_cadastro']
    search_fields = ['nome_produto', 'descricao', 'fabricante']
    readonly_fields = ['data_cadastro']

@admin.register(EntradaProduto)
class EntradaProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo_produto', 'quantidade', 'valor_nota', 'numero_nota_fiscal', 'data']
    list_filter = ['data', 'codigo_produto__fabricante']
    search_fields = ['codigo_produto__nome_produto', 'numero_nota_fiscal', 'id_equipamento']
    readonly_fields = ['data_entrada']
