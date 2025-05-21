from django.contrib import admin
from . import models

# Configuração para exibir os modelos no admin

# Admin personalizado para o modelo Requisicoes
class RequisicoesAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'endereco', 'cnpj', 'contrato', 'inicio_de_contrato', 
        'vigencia', 'data', 'motivo', 'envio', 'comercial', 'tipo_produto',
        'carregador', 'cabo', 'tipo_fatura', 'valor_unitario', 'valor_total',
        'forma_pagamento', 'observacoes', 'TP', 'status_faturamento', 
        'id_equipamentos', 'numero_de_equipamentos', 'aos_cuidados'
    )
    search_fields = ('nome',)  # Campo de pesquisa para o admin

admin.site.register(models.Requisicoes, RequisicoesAdmin)


# Inline do Equipamfrom django.contrib import admin
from .models import ControleModel
from django.contrib import admin
from .models import ControleModel

class ControleModelAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'iccid_equipamento1', 'id_equipamento1', 'iccid_equipamento2', 'id_equipamento2', 
                    'iccid_equipamento3', 'id_equipamento3', 'iccid_equipamento4', 'id_equipamento4', 
                    'iccid_equipamento5', 'id_equipamento5', 'iccid_equipamento6', 'id_equipamento6', 
                    'iccid_equipamento7', 'id_equipamento7', 'iccid_equipamento8', 'id_equipamento8', 
                    'iccid_equipamento9', 'id_equipamento9', 'iccid_equipamento10', 'id_equipamento10', 'quantidade')

admin.site.register(ControleModel, ControleModelAdmin)
