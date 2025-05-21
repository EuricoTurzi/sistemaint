from django.contrib import admin

# Register your models here.
from . import models 

class estoqueadmin(admin.ModelAdmin):
    list_display = ('produto', 'descricao',)
    search_fields = ('produto',)

admin.site.register(models.Estoque,estoqueadmin)


