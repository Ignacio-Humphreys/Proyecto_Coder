from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("Cursos", views.cursos, name="Cursos"),
    path("Profesores", views.profesores, name="Profesores"),
    path("Estudiantes", views.estudiantes, name="Estudiantes"),
    path("Entregables", views.entregables, name="Entregables"),
]