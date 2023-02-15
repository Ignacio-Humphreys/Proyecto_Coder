from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("Cursos/", views.cursos, name="Cursos"),
    path("Profesores/", views.profesores, name="Profesores"),
    path("Estudiantes/", views.estudiantes, name="Estudiantes"),
    path("Entregables/", views.entregables, name="Entregables"),
    path("cursoFormulario/", views.cursoFormulario, name="cursoFormulario"),
    path("profesorFormulario/", views.profesorFormulario, name="profesorFormulario"),
    path("busquedaCamada/", views.busquedaCamada, name="busquedaCamada"),
    path("buscar/", views.buscar),
]