from django import forms
from .models import Lembrete

class LembreteForm(forms.ModelForm):
    class Meta:
        model = Lembrete
        fields = [
             'titulo', 'descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'})
        }