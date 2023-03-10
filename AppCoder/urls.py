from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("Cursos/", views.cursos, name="Cursos"),
    path("Profesores/", views.profesores, name="Profesores"),
    path("Estudiantes/", views.estudiantes, name="Estudiantes"),
    path("Entregables/", views.entregables, name="Entregables"),
    path("cursoFormulario/", views.cursoFormulario, name="CursoFormulario"),
    path("profesorFormulario/", views.profesorFormulario, name="ProfesorFormulario"),
    path("busquedaCamada/", views.busquedaCamada, name="BusquedaCamada"),
    path("buscar/", views.buscar),
    path("leerProfesores/", views.leerProfesores, name="LeerProfesores"),
    path("borrarProfesores/<profesor_nombre>", views.borrarProfesores, name="borrarProfesores"),
    path("editarProfesores/<profesor_nombre>", views.editarProfesores, name="editarProfesores"),
    path("cursos_list/", views.CursoList.as_view(), name="List"),
    path(r'˄(?P<pk>\d+)$', views.CursoDetalle.as_view(), name="Detail"),
    path(r'˄nuevo$', views.CursoCreacion.as_view(), name="New"),
    path(r'˄editar/˄(?P<pk>\d+)$$', views.CursoUpdate.as_view(), name="Edit"),
    path(r'˄borrar/˄(?P<pk>\d+)$$', views.CursoDelete.as_view(), name="Delete"),
    path("login", views.login_request, name="Login"),
    path("registro", views.register, name="Register"),
    path("logout", LogoutView.as_view(template_name="../templates/AppCoder/logout.html"), name="Logout"),
    path("editarPerfil", views.editarPerfil, name="editarPerfil"),
    path("agregarAvatar", views.agregarAvatar, name="AgregarAvatar"),
]