from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Carreras
    path('carreras/', views.carrera_lista, name='carrera_lista'),
    path('carreras/nueva/', views.carrera_gestion, name='carrera_crear'),
    path('carreras/editar/<int:pk>/', views.carrera_gestion, name='carrera_editar'),
    path('carreras/eliminar/<int:pk>/', views.carrera_eliminar, name='carrera_eliminar'),

    # Profesores
    path('profesores/', views.profesor_lista, name='profesor_lista'),
    path('profesores/nuevo/', views.profesor_gestion, name='profesor_crear'),
    path('profesores/editar/<int:pk>/', views.profesor_gestion, name='profesor_editar'),
    path('profesores/eliminar/<int:pk>/', views.profesor_eliminar, name='profesor_eliminar'),

    # Estudiantes
    path('estudiantes/', views.estudiante_lista, name='estudiante_lista'),
    path('estudiantes/nuevo/', views.estudiante_gestion, name='estudiante_crear'),
    path('estudiantes/editar/<int:pk>/', views.estudiante_gestion, name='estudiante_editar'),
    path('estudiantes/eliminar/<int:pk>/', views.estudiante_eliminar, name='estudiante_eliminar'),

    # Materias
    path('materias/', views.materia_lista, name='materia_lista'),
    path('materias/nueva/', views.materia_gestion, name='materia_crear'),
    path('materias/editar/<int:pk>/', views.materia_gestion, name='materia_editar'),
    path('materias/eliminar/<int:pk>/', views.materia_eliminar, name='materia_eliminar'),

    # Aulas
    path('aulas/', views.aula_lista, name='aula_lista'),
    path('aulas/nueva/', views.aula_gestion, name='aula_crear'),
    path('aulas/editar/<int:pk>/', views.aula_gestion, name='aula_editar'),
    path('aulas/eliminar/<int:pk>/', views.aula_eliminar, name='aula_eliminar'),

    # Periodos
    path('periodos/', views.periodo_lista, name='periodo_lista'),
    path('periodos/nuevo/', views.periodo_gestion, name='periodo_crear'),
    path('periodos/editar/<int:pk>/', views.periodo_gestion, name='periodo_editar'),
    path('periodos/eliminar/<int:pk>/', views.periodo_eliminar, name='periodo_eliminar'),

    # Horarios
    path('horarios/', views.horario_lista, name='horario_lista'),
    path('horarios/nuevo/', views.horario_gestion, name='horario_crear'),
    path('horarios/editar/<int:pk>/', views.horario_gestion, name='horario_editar'),
    path('horarios/eliminar/<int:pk>/', views.horario_eliminar, name='horario_eliminar'),

    # Grupos
    path('grupos/', views.grupo_lista, name='grupo_lista'),
    path('grupos/nuevo/', views.grupo_gestion, name='grupo_crear'),
    path('grupos/editar/<int:pk>/', views.grupo_gestion, name='grupo_editar'),
    path('grupos/eliminar/<int:pk>/', views.grupo_eliminar, name='grupo_eliminar'),
    path('grupos/detalle/<int:pk>/', views.grupo_detalle, name='grupo_detalle'),

    # Calificaciones
    path('calificaciones/', views.calificacion_lista, name='calificacion_lista'),
    path('calificaciones/nueva/', views.calificacion_gestion, name='calificacion_crear'),
    path('calificaciones/editar/<int:pk>/', views.calificacion_gestion, name='calificacion_editar'),
    path('calificaciones/eliminar/<int:pk>/', views.calificacion_eliminar, name='calificacion_eliminar'),
    path('boleta/<int:pk>/', views.boleta_estudiante, name='boleta_estudiante'),
]
