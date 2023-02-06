from django.db import models #Viene x default y ya trae el constructor dentro, por eso no se crea un __init__ ni nada

# Create your models here.
class Curso(models.Model): #Importo el modelo del módulo models de django
    nombre = models.CharField(max_length=40) #Indica que va a ser un campo de texto
    comision = models.IntegerField() #Indica que va a ser números enteros

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField() #Porque solo busco un True o False