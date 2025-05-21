from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','endereco','cnpj','inicio_de_contrato','vigencia','termino']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class' : 'form-control', 'rows':3}),
            'cnpj': forms.Textarea(attrs={'class' : 'form-control', 'rows':3}),
            'inicio_de_contrato': forms.Textarea(attrs={'class' : 'form-control', 'rows':3}),
            'vigencia': forms.Select(attrs={'class': 'form-control'}),
            'termino': forms.Textarea(attrs={'class' : 'form-control', 'rows':3}),
            'equipamento': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.Textarea(attrs={'class' : 'form-control', 'rows':1}),
        
        }
        