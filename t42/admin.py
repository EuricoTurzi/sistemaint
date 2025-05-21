from django.contrib import admin
from .models import T42Model

class T42ModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id_equipamento', 'data', 'status','estoque_status')  # Inclua todos os campos visíveis
    list_filter = ('nome', 'status')  # Filtrar por nome e status
    search_fields = ('id_equipamento', 'nome__nome')  # Ajuste conforme o campo relacionado
    ordering = ('-data',)  # Use um campo existente, como 'data'
    date_hierarchy = 'data'  # Usar o campo 'data' para hierarquia de datas

    # Se você deseja personalizar os campos do formulário no admin
    fields = ('nome', 'id_equipamento', 'data', 'status')  # Inclua todos os campos

admin.site.register(T42Model, T42ModelAdmin)