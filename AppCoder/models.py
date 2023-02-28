from django.db import models #Viene x default y ya trae el constructor dentro, por eso no se crea un __init__ ni nada
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model): #Importo el modelo del módulo models de django
    nombre = models.CharField(max_length=40) #Indica que va a ser un campo de texto
    comision = models.IntegerField() #Indica que va a ser números enteros
    def __str__(self):
        return f"Nombre: {self.nombre} - Comisión: {self.comision}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Profesión: {self.profesion}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField() #Porque solo busco un True o False
    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha de entrega: {self.fechaDeEntrega} - Entregado?: {self.entregado}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #Vinculo con el usuario
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True) #Subcarpeta con los avatares