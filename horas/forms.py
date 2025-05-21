from django import forms
from .models import horas

class HorasForm(forms.ModelForm):
    class Meta:
        model = horas
        fields = [
            'funcionario',
            'hora_inicial',
            'comprovante1',
            'hora_final',
            'comprovante2',
            'motivo',
            'total'
        ]
        widgets = {
            'funcionario': forms.Select(attrs={'class': 'form-control'}),
            'comprovante1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'hora_inicial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AAAA-MM-DD HH:MM:SS'}),
            'hora_final': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AAAA-MM-DD HH:MM:SS'}),
            'comprovante2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'motivo': forms.TextInput(attrs={'class': 'form-control'}),
            'total': forms.TextInput(attrs={'class': 'form-control'}),
        }
