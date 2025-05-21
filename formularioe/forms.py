from django import forms
from .models import formularioe, Clientes

class formularioeForm(forms.ModelForm):
    class Meta:
        model = formularioe
        fields = ['nome','tipo_entrada','tipo_produto','tipo_customizacao','recebimento','entregue_por_retirado_por','id_equipamentos']
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-control'}),
            'tipo_entrada': forms.Select(attrs={'class': 'form-control'}),
            'tipo_produto': forms.Select(attrs={'class': 'form-control'}),
            'tipo_customizacao': forms.Select(attrs={'class': 'form-control'}),
            'recebimento': forms.Select(attrs={'class': 'form-control'}),
            'entregue_por_retirado_por' : forms.TextInput(attrs={'class': 'form-control'}),
            'id_equipamentos' : forms.TextInput(attrs={'class': 'form-control'}),
           
        }



