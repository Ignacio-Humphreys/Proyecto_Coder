from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate #Para poder loguearse
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required
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
            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
            profesor.save() #Guarda en base de datos
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

#CRUD
def leerProfesores(request):
    profesores = Profesor.objects.all() #Traigo a los profesores
    contexto = {"profesores":profesores}
    return render(request, "../templates/AppCoder/leerProfesores.html", contexto)

def borrarProfesores(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre = profesor_nombre)
    profesor.delete()

    #Lee nuevamente a los profesores. Podría hacer leerProfesores()
    profesores = Profesor.objects.all()
    contexto = {"profesores":profesores}
    return render(request, "../templates/AppCoder/leerProfesores.html", contexto)

def editarProfesores(request, profesor_nombre): #Modifica pero termina creando un nuevo profesor

    profesor = Profesor.objects.get(nombre = profesor_nombre)

    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario) #Formulario vacío

        if miFormulario.is_valid: #Chequea si es válido
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
            profesor.save() #Guarda en base de datos
            return render(request, "../templates/AppCoder/inicio.html")
    
    else:
        miFormulario = ProfesorFormulario(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email, "profesion":profesor.profesion})
    
    return render(request, "../templates/AppCoder/editarProfesores.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})

class CursoList(ListView): #Clases basadas en vistas
    model = Curso
    template_name = "../templates/AppCoder/cursos_list.html"

class CursoDetalle(DetailView): #Detalle de cada curso
    model = Curso
    template_name = "../templates/AppCoder/curso_detalle.html"

class CursoCreacion(CreateView): #Creo cursos
    model = Curso
    success_url = "../cursos_list/" #Me dice que no existe...
    fields = ["nombre", "comision"]

class CursoUpdate(UpdateView): #Actualizo cursos
    model = Curso
    success_url = "../cursos_list/"
    fields = ["nombre", "comision"]

class CursoDelete(DeleteView): #Borro cursos
    model = Curso
    success_url = "../cursos_list/"
    
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid(): #Chequea si es válido
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = contra)

            if user is not None: #Si el usuario no está vacío
                login(request, user) #Intenta el logueo
                return render(request, "../templates/AppCoder/inicio.html", {"Mensaje":f"Bienvenido {usuario}"}) #Logueo exitoso
            else:
                return render(request, "../templates/AppCoder/inicio.html", {"Mensaje":f"Datos incorrectos"}) #Logueo fallido
        
        else:
            return render(request, "../templates/AppCoder/inicio.html", {"Mensaje":f"Error, formulario incorrecto"})
    
    form = AuthenticationForm() #Si hay error me vuelve al autenticador
    return render(request, "../templates/AppCoder/login.html", {"form":form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "../templates/AppCoder/inicio.html", {"Mensaje":f"Usuario creado: {username}"})

    else:
        form = UserRegisterForm()

    return render(request, "../templates/AppCoder/registro.html", {"form":form})

@login_required
def editarPerfil(request):

    usuario = request.user #Usuario logueado

    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            #Datos a modificar
            usuario.email = informacion["email"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password2"]
            usuario.save()

            return render(request, "../templates/AppCoder/inicio.html")

    else:
        miFormulario = UserEditForm(initial={"email":usuario.email})

    return render(request, "../templates/AppCoder/editarPerfil.html",{"miFormulario":miFormulario, "usuario":usuario})