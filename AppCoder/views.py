from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import *

# Create your views here.
def vistaCurso(self):
    curso = Curso(nombre = "Desarrollo Web", comision = 19800)
    curso.save()
    docDeTexto = f"--> Curso: {curso.nombre} --> Comisión: {curso.comision}"
    return HttpResponse(docDeTexto)