from django import forms
from .models import T42Model

class T42Form(forms.ModelForm):
    class Meta:
        model = T42Model
        fields = ['nome', 'equipamento','id_equipamento', 'status','estoque_status','fazenda']

        widgets = {
            'nome': forms.Select(attrs={'class': 'form-control'}),
            'equipamento': forms.Select(attrs={'class': 'form-control'}),
            'id_equipamento': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'fazenda':forms.TextInput(attrs={'class': 'form-control'}),
            'estoque_status': forms.Select(attrs={'class': 'form-control'}),
        }
