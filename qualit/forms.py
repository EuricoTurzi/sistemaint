from django import forms
from .models import Qualit

from django import forms
from .models import Qualit

class QualitForm(forms.ModelForm):
    class Meta:
        model = Qualit
        fields = [
            'Data', 'ID', 'ID2', 'ICCID_NOVO', 'CONTRATO', 'OPERADORA', 'CLIENTE'
        ]
        widgets = {
            'Data': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a data'}),
            'ID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o ID'}),
            'ID2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o ID2'}),
            'ICCID_NOVO': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o ICCID Novo'}),
            'CONTRATO': forms.Select(attrs={'class': 'form-control'}),
            'OPERADORA': forms.Select(attrs={'class': 'form-control'}),
            'CLIENTE': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o cliente'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Adicione placeholders dinâmicos ou personalizações adicionais, se necessário
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        # Defina valores iniciais ou lógica específica para certos campos
        self.fields['CONTRATO'].empty_label = "Selecione o contrato"
        self.fields['OPERADORA'].empty_label = "Selecione a operadora"
