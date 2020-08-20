from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True, help_text='Requis.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optionnel.')
    email = forms.EmailField(max_length=254, help_text='Requis. Merci de fournir une adresse valide')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )