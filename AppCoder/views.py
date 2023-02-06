from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import *

# Create your views here.
def inicio(request):
    return render(request, "../templates/AppCoder/inicio.html")

def cursos(request):
    return render(request, "../templates/AppCoder/cursos.html")

def profesores(request):
    return render(request, "../templates/AppCoder/profesores.html")

def entregables(request):
    return render(request, "../templates/AppCoder/entregables.html")

def estudiantes(request):
    return render(request, "../templates/AppCoder/estudiantes.html")