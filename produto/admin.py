from django.contrib import admin

# Register your models here.
from . import models 

class produtoadmin(admin.ModelAdmin):
    list_display = ('nome','quantidade')
    search_fields = ('nome',)

admin.site.register(models.Produto,produtoadmin)
