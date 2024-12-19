from django import forms
from . import models
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Formulario para criar usauario
class RegisterUser(UserCreationForm):
    first_name = forms.CharField(
        label="Primeiro nome",
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        label="Sobrenome",
        required=True,
        min_length=3,
    )
    email = forms.EmailField()

    username=forms.CharField(
        label="Nome de Usuario",
        required=True,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )