from django.contrib import admin
from .models import Transportadora, formulario_divisao, estoque_tuper

class TransportadoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj',)
    search_fields = ('nome',)

class FormularioDivisaoAdmin(admin.ModelAdmin):
    list_display = ('transportadora', 'destino', 'quantidade', 'tipo_produto', 'Id_equipamentos',)
    search_fields = ('transportadora', 'destino', 'tipo_produto',)

class EstoqueTuperAdmin(admin.ModelAdmin):
    list_display = ('tipo_produto', 'quantidade',)
    search_fields = ('tipo_produto',)

admin.site.register(Transportadora, TransportadoraAdmin)
admin.site.register(formulario_divisao, FormularioDivisaoAdmin)
admin.site.register(estoque_tuper, EstoqueTuperAdmin)