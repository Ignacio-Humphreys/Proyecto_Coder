from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import *

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

"""def cursoFormulario(request):
    if request.method == "POST":
        curso = Curso(request.POST["curso"], request.POST["camada"])
        curso.save()
        return render(request, "../templates/AppCoder/inicio.html")
    return render(request, "../templates/AppCoder/cursoFormulario.html")"""

def cursoFormulario(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario) #Formulario vacío

        if miFormulario.is_valid: #Chequea si es válido
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], comision=informacion["camada"])
            curso.save() #Guarda en base de datos
            return render(request, "../templates/AppCoder/inicio.html")
    
    else:
        miFormulario = CursoFormulario()
    
    return render(request, "../templates/AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})

def profesorFormulario(request):
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario) #Formulario vacío

        if miFormulario.is_valid: #Chequea si es válido
            informacion = miFormulario.cleaned_data
            curso = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
            curso.save() #Guarda en base de datos
            return render(request, "../templates/AppCoder/inicio.html")
    
    else:
        miFormulario = ProfesorFormulario()
    
    return render(request, "../templates/AppCoder/profesorFormulario.html", {"miFormulario":miFormulario})

def busquedaCamada(request):
     return render(request, "../templates/AppCoder/busquedaCamada.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(comision__icontains=camada)

        return render(request, "../templates/AppCoder/resultadosBusqueda.html", {"cursos":cursos, "camada":camada})

    else:
        respuesta = "Datos no enviados"
        
    return HttpResponse(respuesta)