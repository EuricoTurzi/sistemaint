from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from . import models 

class manutensaolistadmin(admin.ModelAdmin):
    list_display = ('customizacao',
                'numero_equipamento','imagem')
    

    def imagen(self, obj):
        return obj.imagem


admin.site.register(models.manutensaolis,manutensaolistadmin)