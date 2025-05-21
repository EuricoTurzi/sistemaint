from django import forms
from .models import Estoque
from django.core.exceptions import ValidationError

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['produto', 'descricao', 'preco', 'marca', 'quantidade']
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')
        nome = self.cleaned_data.get('nome')

        if quantidade < 0:
            raise ValidationError('A quantidade não pode ser negativa.')
        return quantidade
