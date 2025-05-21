from django import forms
from .models import Formulario

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['razao_social', 'cnpj', 'inicio_de_contrato', 'vigencia']
        widgets = {
            'razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'inicio_de_contrato': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'vigencia': forms.TextInput(attrs={'class': 'form-control'}),
        }
        permissions = [
            ("view_formulario", "Can view formulario"),
            ("add_formulario", "Can add formulario"),
            ("change_formulario", "Can change formulario"),
            ("delete_formulario", "Can delete formulario"),
        ]