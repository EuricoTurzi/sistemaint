from django.contrib import admin

# Register your models here.
from . import models 

class clientesadmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco','cnpj','inicio_de_contrato','vigencia','termino')
    search_fields = ('nome',)

admin.site.register(models.Cliente,clientesadmin)