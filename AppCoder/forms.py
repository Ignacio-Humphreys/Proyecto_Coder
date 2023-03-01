from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):
    #Especificar los campos
    curso = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}

class UserEditForm(UserCreationForm): #Qué se va a modificar del usuario
    email = forms.EmailField(label="Modificar el email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetí tu contraseña", widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k: "" for k in fields} #Quito los msjs de ayuda

class AvatarFormulario(UserCreationForm):
    imagen = forms.ImageField()
    password1 = None
    password2 = None

    class Meta:
        model = User
        fields = ["imagen"]
        help_texts = {k: "" for k in fields}