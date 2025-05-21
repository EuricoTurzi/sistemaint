from django.contrib import admin
from .models import Reativacao, IdIccid

class ReativacaoListAdmin(admin.ModelAdmin):
    list_display = ('nome', 'motivo_reativacao', 'canal_solicitacao','cnpj', 'observacoes','status_reativacao')

admin.site.register(Reativacao, ReativacaoListAdmin)

class IdIccidListAdmin(admin.ModelAdmin):
    list_display = ('reativacao', 'id_equipamentos', 'ccid_equipamentos')

admin.site.register(IdIccid, IdIccidListAdmin)
