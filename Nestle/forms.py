# forms.py
from django import forms
from .models import GridInternacional

class GridInternacionalForm(forms.ModelForm):
    class Meta:
        model = GridInternacional
        fields = [
            "cliente",
            "local_de_entrega",
            "modelo",
            "id_planilha",
            "ccid",
            "sla_insercao",
            "data_insercao",
            "destino",
            "bl",
            "container",
            "sla_viagem",
            "data_chegada_destino",
            "sla_retirada",
            "data_retirada",
            "sla_envio_brasil",
            "data_envio_brasil",
            "sla_chegada_brasil",
            "data_brasil",
            "status_operacao",
            "sla_operacao",
            "reposicao",
            "observacao",
            "data_chegada_porto",
            "data_embarque_maritimo",
            "data_desembarque_maritimo",
            "data_chegada_terminal",
            "data_saida_terminal",
            "sla_porto_nacional",
            "sla_terrestre",
            "sla_maritimo",
            "sla_terminal_internacional",
            "sla_terrestre_internacional",
            "local",
            "status_container",
            "data_desembarque",
            "sla_internacional",
            "ultimo_grid",
        ]
        widgets = {
            "data_insercao": forms.DateInput(attrs={"type": "date"}),
            "data_chegada_destino": forms.DateInput(attrs={"type": "date"}),
            "data_retirada": forms.DateInput(attrs={"type": "date"}),
            "data_envio_brasil": forms.DateInput(attrs={"type": "date"}),
            "data_brasil": forms.DateInput(attrs={"type": "date"}),
            "data_chegada_porto": forms.DateInput(attrs={"type": "date"}),
            "data_embarque_maritimo": forms.DateInput(attrs={"type": "date"}),
            "data_desembarque_maritimo": forms.DateInput(attrs={"type": "date"}),
            "data_chegada_terminal": forms.DateInput(attrs={"type": "date"}),
            "data_saida_terminal": forms.DateInput(attrs={"type": "date"}),
            "data_desembarque": forms.DateInput(attrs={"type": "date"}),
        }
