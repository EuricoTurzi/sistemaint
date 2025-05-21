from django import forms
from .models import Transportadora, formulario_divisao, estoque_tuper

class TransportadoraForm(forms.ModelForm):
    class Meta:
        model = Transportadora
        fields = ['nome', 'cnpj']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['cnpj'].widget.attrs.update({'class': 'form-control'})

class TransregistroForm(forms.ModelForm):
    class Meta:
        model = formulario_divisao
        fields = ['transportadora', 'destino', 'quantidade', 'tipo_produto', 'Id_equipamentos']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['transportadora'].widget.attrs.update({'class': 'form-control'})
        self.fields['destino'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['tipo_produto'].widget.attrs.update({'class': 'form-control'})
        self.fields['Id_equipamentos'].widget.attrs.update({'class': 'form-control'})


class EstoqueTuperForm(forms.ModelForm):
    class Meta:
        model = estoque_tuper
        fields = ['tipo_produto', 'quantidade']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_produto'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantidade'].widget.attrs.update({'class': 'form-control'})