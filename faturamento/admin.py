from django.contrib import admin
from .models import Formulario

class FormularioAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'cnpj', 'inicio_de_contrato', 'vigencia')
    search_fields = ('razao_social', 'cnpj')
    list_filter = ('inicio_de_contrato', 'vigencia')
    ordering = ('razao_social',)

admin.site.register(Formulario, FormularioAdmin)