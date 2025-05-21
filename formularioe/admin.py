from django.contrib import admin
from.import models


# Register your models here.
class formularioesadmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo_entrada','tipo_produto','tipo_customizacao','recebimento','entregue_por_retirado_por','id_equipamentos')
    search_fields = ('nome',)

admin.site.register(models.formularioe,formularioesadmin)