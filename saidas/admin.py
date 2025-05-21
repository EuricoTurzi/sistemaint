from django.contrib import admin

# Register your models here.
from . import models 

class saidasadmin(admin.ModelAdmin):
    list_display = ('produto','data_criacao', 'descricao')
    search_fields = ('produto',)

admin.site.register(models.Saidas,saidasadmin)
