from django import forms
from .models import (Carrera, Profesor, Estudiante, Materia,
                     Aula, PeriodoSemestral, Horario, Grupo, Calificacion)

CSS = {'class': 'form-control'}
CSS_SELECT = {'class': 'form-select'}
CSS_CHECK = {'class': 'form-check-input'}


class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre', 'clave', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs=CSS),
            'clave': forms.TextInput(attrs=CSS),
            'descripcion': forms.Textarea(attrs={**CSS, 'rows': 3}),
        }


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellidos', 'numero_empleado', 'email', 'telefono', 'especialidad']
        widgets = {
            'nombre': forms.TextInput(attrs=CSS),
            'apellidos': forms.TextInput(attrs=CSS),
            'numero_empleado': forms.TextInput(attrs=CSS),
            'email': forms.EmailInput(attrs=CSS),
            'telefono': forms.TextInput(attrs=CSS),
            'especialidad': forms.TextInput(attrs=CSS),
        }


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellidos', 'matricula', 'email', 'telefono', 'carrera', 'fecha_ingreso']
        widgets = {
            'nombre': forms.TextInput(attrs=CSS),
            'apellidos': forms.TextInput(attrs=CSS),
            'matricula': forms.TextInput(attrs=CSS),
            'email': forms.EmailInput(attrs=CSS),
            'telefono': forms.TextInput(attrs=CSS),
            'carrera': forms.Select(attrs=CSS_SELECT),
            'fecha_ingreso': forms.DateInput(attrs={**CSS, 'type': 'date'}),
        }


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'clave', 'creditos', 'carrera', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs=CSS),
            'clave': forms.TextInput(attrs=CSS),
            'creditos': forms.NumberInput(attrs=CSS),
            'carrera': forms.Select(attrs=CSS_SELECT),
            'descripcion': forms.Textarea(attrs={**CSS, 'rows': 3}),
        }


class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ['nombre', 'capacidad', 'ubicacion']
        widgets = {
            'nombre': forms.TextInput(attrs=CSS),
            'capacidad': forms.NumberInput(attrs=CSS),
            'ubicacion': forms.TextInput(attrs=CSS),
        }


class PeriodoSemestralForm(forms.ModelForm):
    class Meta:
        model = PeriodoSemestral
        fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs=CSS),
            'fecha_inicio': forms.DateInput(attrs={**CSS, 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={**CSS, 'type': 'date'}),
            'activo': forms.CheckboxInput(attrs=CSS_CHECK),
        }


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['dia', 'hora_inicio', 'hora_fin']
        widgets = {
            'dia': forms.Select(attrs=CSS_SELECT),
            'hora_inicio': forms.TimeInput(attrs={**CSS, 'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={**CSS, 'type': 'time'}),
        }


class GrupoForm(forms.ModelForm):
    estudiantes = forms.ModelMultipleChoiceField(
        queryset=Estudiante.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        label='Estudiantes inscritos'
    )

    class Meta:
        model = Grupo
        fields = ['nombre', 'profesor', 'materia', 'aula', 'periodo', 'horario', 'estudiantes']
        widgets = {
            'nombre': forms.TextInput(attrs=CSS),
            'profesor': forms.Select(attrs=CSS_SELECT),
            'materia': forms.Select(attrs=CSS_SELECT),
            'aula': forms.Select(attrs=CSS_SELECT),
            'periodo': forms.Select(attrs=CSS_SELECT),
            'horario': forms.Select(attrs=CSS_SELECT),
        }


class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['estudiante', 'grupo', 'calificacion', 'observaciones']
        widgets = {
            'estudiante': forms.Select(attrs=CSS_SELECT),
            'grupo': forms.Select(attrs=CSS_SELECT),
            'calificacion': forms.NumberInput(attrs={**CSS, 'step': '0.1', 'min': '0', 'max': '10'}),
            'observaciones': forms.Textarea(attrs={**CSS, 'rows': 3}),
        }
