from django.contrib import admin
from .models import (Carrera, Profesor, Estudiante, Materia,
                     Aula, PeriodoSemestral, Horario, Grupo, Calificacion)

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('clave', 'nombre')
    search_fields = ('nombre', 'clave')

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('numero_empleado', 'apellidos', 'nombre', 'email', 'especialidad')
    search_fields = ('nombre', 'apellidos', 'numero_empleado')

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'apellidos', 'nombre', 'carrera', 'fecha_ingreso')
    list_filter = ('carrera',)
    search_fields = ('nombre', 'apellidos', 'matricula')

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('clave', 'nombre', 'creditos', 'carrera')
    list_filter = ('carrera',)
    search_fields = ('nombre', 'clave')

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad', 'ubicacion')

@admin.register(PeriodoSemestral)
class PeriodoSemestralAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'activo')
    list_filter = ('activo',)

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('dia', 'hora_inicio', 'hora_fin')
    list_filter = ('dia',)

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'materia', 'profesor', 'aula', 'periodo')
    list_filter = ('periodo', 'materia')
    filter_horizontal = ('estudiantes',)

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'grupo', 'calificacion')
    list_filter = ('grupo',)
    search_fields = ('estudiante__nombre', 'estudiante__apellidos')
