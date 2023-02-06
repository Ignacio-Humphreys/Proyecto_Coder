from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio),
    path("Cursos", views.cursos, name="Cursos"),
    path("Profesores", views.profesores),
    path("Estudiantes", views.estudiantes),
    path("Entregables", views.entregables),
]