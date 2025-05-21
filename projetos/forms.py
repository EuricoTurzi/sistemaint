from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['id_equipamento', 'local', 'operacao']
        widgets = {
            'operacao': forms.Select(attrs={'class': 'form-control'}),
            'id_equipamento': forms.TextInput(attrs={'class': 'form-control'}),
            'local': forms.TextInput(attrs={'class': 'form-control'}),
        }
