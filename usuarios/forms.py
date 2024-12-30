from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class RegistroDeUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {
            key: '' 
            for key in fields
        }

class EditarPerfil(UserChangeForm):
     password = None
     email = forms.EmailField(label='Email', required=False)
     first_name = forms.CharField(label='Nombre', required=False)
     last_name = forms.CharField(label='Apellido', required=False)
     avatar = forms.ImageField(required=False)
     
     class Meta:
         model = User
         fields = ['email', 'first_name', 'last_name', 'avatar']