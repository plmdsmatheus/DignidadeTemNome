from django import forms
from .models import Inscricao

class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        exclude = ['pontuacao']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'renda_familiar': forms.Select(attrs={'class': 'form-select'}),
            'territorio': forms.Select(attrs={'class': 'form-select'}),
            'genero_sexualidade': forms.Select(attrs={'class': 'form-select'}),
            'etnia': forms.Select(attrs={'class': 'form-select'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_civil': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_social': forms.TextInput(attrs={'class': 'form-control'}),
            'rg_numero': forms.TextInput(attrs={'class': 'form-control'}),
            'rg_orgao_expedidor': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'rg_anexo': forms.FileInput(attrs={'class': 'form-control'}),
            'populacao_de_rua': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
