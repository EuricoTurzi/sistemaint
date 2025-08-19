# forms.py
from django import forms
from .models import GridInternacional, clientesNestle, ValorMensalCliente
from .models import Carga
class GridInternacionalForm(forms.ModelForm):
    class Meta:
        model = GridInternacional
        fields = [
            "data_envio",
            "requisicao",   
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
            "data_envoice",
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
            
            "rf_invoice",
            "coleta",
            "liberacao",
            "golden_sat",
        ]
        widgets = {
            "data_envio": forms.DateInput(attrs={"type": "date"}),
            "requisicao": forms.TextInput(attrs={"type": "text"}),
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
            "data_envoice": forms.DateInput(attrs={"type": "date"}),
            "ultimo_grid": forms.TextInput(attrs={"type": "text"}),
            "rf_invoice": forms.TextInput(attrs={"type": "text"}),
            "coleta": forms.DateInput(attrs={"type": "date"}),
            "liberacao": forms.DateInput(attrs={"type": "date"}),
            "golden_sat": forms.DateInput(attrs={"type": "date"}),
        }   



class clientesNestleForm(forms.ModelForm):
    class Meta:
        model = clientesNestle
        fields = [
            "cliente",
            "cnpj",
            "endereco", 
            ]       
        widgets = {
            "cnpj": forms.TextInput(attrs={"type": "text"}),
            "endereco": forms.TextInput(attrs={"type": "text"}),
            "quantidade": forms.TextInput(attrs={"type": "text"}),
            "valor": forms.TextInput(attrs={"type": "text"}),
            "local": forms.TextInput(attrs={"type": "text"}),
        }

class ValorMensalForm(forms.ModelForm):
    class Meta:
        model = ValorMensalCliente
        fields = ['valor', 'enviado']
        widgets = {
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'enviado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            # já defini Select acima; agora cuido do resto
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'

class CargaForm(forms.ModelForm):
    class Meta:
        model  = Carga
        fields = [
            'data', 'tipo_transportadora', 'frete_all_in_moeda',
            'frete_all_in_valor', 'frete_all_in_usd',
            'honorarios', 'frete_rodoviario',
            'licenca_importacao', 'taxa_siscomex',
            'taxa_armazenagem',
            'rf_invoice',
            'data_invoice',
            'origem',
            'qtd_equipamento',
        ]
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'frete_all_in_moeda': forms.Select(attrs={'class': 'form-control'}),
            'tipo_transportadora': forms.Select(attrs={'class': 'form-control'}),
            'data_invoice': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            # já defini Select acima; agora cuido do resto
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
    
