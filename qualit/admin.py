from django.contrib import admin
from .models import Qualit
from django.contrib import admin
from .models import Qualit

class QualitAdmin(admin.ModelAdmin):
    list_display = [
        'Data', 'ID', 'ID2', 'ICCID_NOVO', 'CONTRATO', 'OPERADORA', 'CLIENTE'
    ]

admin.site.register(Qualit, QualitAdmin)
