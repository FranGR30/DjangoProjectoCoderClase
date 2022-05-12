from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name = "inicio"),
    path('estudiantes/', estudiantes, name = "estudiantes"),
    path('cursos/', cursos, name = "cursos"),
    path('entregables/', entregables, name = "entregables"),
    #path('cursosFormulario/', cursoFormulario, name = "cursosFormulario"),
    path('busquedaComision/', busquedaComision, name = "busquedaComision"),
    path('buscar/', buscar),
    path('profesores/', leerProfesores, name = "profesores"),
    path('eliminarProfesor/<nombre>', eliminarProfesor, name = "eliminarProfesor"),
    path('editarProfesor/<nombre>', editarProfesor, name = "editarProfesor"),

    path('estudiante/list/',EstudiantesList.as_view(), name = 'estudiante_listar'),
    path('estudiante/<pk>',EstudianteDetalle.as_view(), name = 'estudiante_detalle'),
    path('estudiante/nuevo/',EstudianteCreacion.as_view(), name = 'estudiante_crear'),
    path('estudiante/editar/<pk>',EstudiantesEdicion.as_view(), name = 'estudiante_editar'),
    path('estudiante/borrar/<pk>',EstudiantesEliminacion.as_view(), name = 'estudiante_borrar'),

]
