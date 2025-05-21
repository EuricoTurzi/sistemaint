from django import forms
from .models import Saidas
from django.core.exceptions import ValidationError

class SaidasForm(forms.ModelForm):
    class Meta:
        model = Saidas
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
        produto = self.cleaned_data.get('produto')

        if quantidade > produto.quantidade:
            raise ValidationError(
                f'A quantidade disponível do produto {produto.nome} é de {produto.quantidade} unidades.'
            )
        return quantidade
