from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *

# Formulario para criar usauario
class RegisterUser(UserCreationForm):
    first_name = forms.CharField(
        label="Primeiro nome:",
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        label="Sobrenome:",
        required=True,
        min_length=3,
    )
    email = forms.EmailField(
        label="email:"
    )

    username=forms.CharField(
        label="Nome de Usuario:",
        required=True,
    )
    
    password1 = forms.CharField(
        label="Senha:",
        widget=forms.PasswordInput(attrs={
        'class': 'form-control',  # Classe CSS (opcional)
        'placeholder': 'Digite sua senha'  # Placeholder (opcional)
    }),
)
    password2 = forms.CharField(
        label="Repita sua senha:",
        widget=forms.PasswordInput(attrs={
        'class': 'form-control',  # Classe CSS (opcional)
    }),
)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )
        
class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = ['titulo', 'descricao', 'data_vencimento', 'prioridade', 'status']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título da tarefa'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Digite a descrição da tarefa'
            }),
            'data_vencimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'prioridade': forms.Select(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'data_vencimento': 'Data de Vencimento',
            'prioridade': 'Prioridade',
            'status': 'Status',
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if len(titulo) < 3:
            raise forms.ValidationError("O título deve ter pelo menos 3 caracteres.")
        return titulo