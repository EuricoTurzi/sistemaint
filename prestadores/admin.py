from django.contrib import admin
from.import models


# Register your models here.
class prestadoresadmin(admin.ModelAdmin):
    list_display = ('nome', 'franquia_km','franquiah','valor_acionamento','valorkm','valor_exedente')
    search_fields = ('nome',)

admin.site.register(models.Prestador,prestadoresadmin)