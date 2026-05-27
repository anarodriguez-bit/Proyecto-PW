from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import (Carrera, Profesor, Estudiante, Materia,
                     Aula, PeriodoSemestral, Horario, Grupo, Calificacion)
from .forms import (CarreraForm, ProfesorForm, EstudianteForm, MateriaForm,
                    AulaForm, PeriodoSemestralForm, HorarioForm, GrupoForm, CalificacionForm)


def home(request):
    context = {
        'total_profesores': Profesor.objects.count(),
        'total_estudiantes': Estudiante.objects.count(),
        'total_materias': Materia.objects.count(),
        'total_grupos': Grupo.objects.count(),
        'total_carreras': Carrera.objects.count(),
        'total_aulas': Aula.objects.count(),
        'periodo_activo': PeriodoSemestral.objects.filter(activo=True).first(),
    }
    return render(request, 'home.html', context)


# ─── CARRERAS ─────────────────────────────────────────────────────────────────

def carrera_lista(request):
    carreras = Carrera.objects.all()
    return render(request, 'carreras/lista.html', {'carreras': carreras})

def carrera_gestion(request, pk=None):
    obj = get_object_or_404(Carrera, pk=pk) if pk else None
    accion = 'Editar' if obj else 'Nueva'
    form = CarreraForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Carrera {"actualizada" if obj else "registrada"} correctamente.')
        return redirect('carrera_lista')
    return render(request, 'carreras/form.html', {'form': form, 'accion': accion})

def carrera_eliminar(request, pk):
    obj = get_object_or_404(Carrera, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Carrera eliminada correctamente.')
        return redirect('carrera_lista')
    return render(request, 'carreras/confirmar_eliminar.html', {'objeto': obj, 'tipo': 'Carrera'})


# ─── PROFESORES ───────────────────────────────────────────────────────────────

def profesor_lista(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores/lista.html', {'profesores': profesores})

def profesor_gestion(request, pk=None):
    obj = get_object_or_404(Profesor, pk=pk) if pk else None
    accion = 'Editar' if obj else 'Nuevo'
    form = ProfesorForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Profesor {"actualizado" if obj else "registrado"} correctamente.')
        return redirect('profesor_lista')
    return render(request, 'profesores/form.html', {'form': form, 'accion': accion})

def profesor_eliminar(request, pk):
    obj = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Profesor eliminado correctamente.')
        return redirect('profesor_lista')
    return render(request, 'profesores/confirmar_eliminar.html', {'objeto': obj, 'tipo': 'Profesor'})


# ─── ESTUDIANTES ──────────────────────────────────────────────────────────────

def estudiante_lista(request):
    estudiantes = Estudiante.objects.select_related('carrera').all()
    return render(request, 'estudiantes/lista.html', {'estudiantes': estudiantes})

def estudiante_gestion(request, pk=None):
    obj = get_object_or_404(Estudiante, pk=pk) if pk else None
    accion = 'Editar' if obj else 'Nuevo'
    form = EstudianteForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Estudiante {"actualizado" if obj else "registrado"} correctamente.')
        return redirect('estudiante_lista')
    return render(request, 'estudiantes/form.html', {'form': form, 'accion': accion})

def estudiante_eliminar(request, pk):
    obj = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Estudiante eliminado correctamente.')
        return redirect('estudiante_lista')
    return render(request, 'estudiantes/confirmar_eliminar.html', {'objeto': obj, 'tipo': 'Estudiante'})


# ─── MATERIAS ─────────────────────────────────────────────────────────────────

def materia_lista(request):
    materias = Materia.objects.select_related('carrera').all()
    return render(request, 'materias/lista.html', {'materias': materias})

def materia_gestion(request, pk=None):
    obj = get_object_or_404(Materia, pk=pk) if pk else None
    accion = 'Editar' if obj else 'Nueva'
    form = MateriaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Materia {"actualizada" if obj else "registrada"} correctamente.')
        return redirect('materia_lista')
    return render(request, 'materias/form.html', {'form': form, 'accion': accion})

def materia_eliminar(request, pk):
    obj = get_object_or_404(Materia, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Materia eliminada correctamente.')
        return redirect('materia_lista')
    return render(request, 'materias/confirmar_eliminar.html', {'objeto': obj, 'tipo': 'Materia'})


# ─── AULAS ────────────────────────────────────────────────────────────────────

def aula_lista(request):
    aulas = Aula.objects.all()
    return render(request, 'aulas/lista.html', {'aulas': aulas})

def aula_gestion(request, pk=None):
    obj = get_object_or_404(Aula, pk=pk) if pk else None
    accion = 'Editar' if obj else 'Nueva'
    form = AulaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Aula {"actualizada" if obj else "registrada"} correctamente.')
        return redirect('aula_lista')
    return render(request, 'aulas/form.html', {'form': form, 'accion': accion})

def aula_eliminar(request, pk):
    obj = get_object_or_404(Aula, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Aula eliminada correctamente.')
        return redirect('aula_lista')
    return render(request, 'aulas/confirmar_eliminar.html', {'objeto': obj, 'tipo': 'Aula'})


# ─── PERIODOS SEMESTRALES ─────────────────────────────────────────────────────

def periodo_lista(request):
    periodos = PeriodoSemestral.objects.all()
    return render(request, 'periodos/lista.html', {'periodos': periodos})

def periodo_gestion(request, pk=None):
    obj = get_object_or_404(PeriodoSemestral, pk=pk) if pk else None
    accion = 'Editar' if obj else 'Nuevo'
    form = PeriodoSemestralForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Periodo {"actualizado" if obj else "registrado"} correctamente.')
        return redirect('periodo_lista')
    return render(request, 'periodos/form.html', {'form': form, 'accion': accion})

def periodo_eliminar(request, pk):
    obj = get_object_or_404(PeriodoSemestral, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Periodo eliminado correctamente.')
        return redirect('periodo_lista')
    return render(request, 'periodos/confirmar_eliminar.html', {'objeto': obj, 'tipo': 'Periodo'})


# ─── HORARIOS ─────────────────────────────────────────────────────────────────

def horario_lista(request):
    horarios = Horario.objects.all()
    return render(request, 'horarios/lista.html', {'horarios': horarios})

def horario_gestion(request, pk=None):
    obj = get_object_or_404(Horario, pk=pk) if pk else None
    accion = 'Editar' if obj else 'Nuevo'
    form = HorarioForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Horario {"actualizado" if obj else "registrado"} correctamente.')
        return redirect('horario_lista')
    return render(request, 'horarios/form.html', {'form': form, 'accion': accion})

def horario_eliminar(request, pk):
    obj = get_object_or_404(Horario, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Horario eliminado correctamente.')
        return redirect('horario_lista')
    return render(request, 'horarios/confirmar_eliminar.html', {'objeto': obj, 'tipo': 'Horario'})


# ─── GRUPOS ───────────────────────────────────────────────────────────────────

def grupo_lista(request):
    grupos = Grupo.objects.select_related('profesor', 'materia', 'aula', 'periodo', 'horario').all()
    return render(request, 'grupos/lista.html', {'grupos': grupos})

def grupo_gestion(request, pk=None):
    obj = get_object_or_404(Grupo, pk=pk) if pk else None
    accion = 'Editar' if obj else 'Nuevo'
    form = GrupoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Grupo {"actualizado" if obj else "registrado"} correctamente.')
        return redirect('grupo_lista')
    return render(request, 'grupos/form.html', {'form': form, 'accion': accion})

def grupo_eliminar(request, pk):
    obj = get_object_or_404(Grupo, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Grupo eliminado correctamente.')
        return redirect('grupo_lista')
    return render(request, 'grupos/confirmar_eliminar.html', {'objeto': obj, 'tipo': 'Grupo'})

def grupo_detalle(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    calificaciones = Calificacion.objects.filter(grupo=grupo).select_related('estudiante')
    return render(request, 'grupos/detalle.html', {'grupo': grupo, 'calificaciones': calificaciones})


# ─── CALIFICACIONES ───────────────────────────────────────────────────────────

def calificacion_lista(request):
    calificaciones = Calificacion.objects.select_related('estudiante', 'grupo').all()
    return render(request, 'calificaciones/lista.html', {'calificaciones': calificaciones})

def calificacion_gestion(request, pk=None):
    obj = get_object_or_404(Calificacion, pk=pk) if pk else None
    accion = 'Editar' if obj else 'Nueva'
    form = CalificacionForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Calificación {"actualizada" if obj else "registrada"} correctamente.')
        return redirect('calificacion_lista')
    return render(request, 'calificaciones/form.html', {'form': form, 'accion': accion})

def calificacion_eliminar(request, pk):
    obj = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Calificación eliminada correctamente.')
        return redirect('calificacion_lista')
    return render(request, 'calificaciones/confirmar_eliminar.html', {'objeto': obj, 'tipo': 'Calificación'})


# ─── BOLETA DE CALIFICACIONES ─────────────────────────────────────────────────

def boleta_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    periodo_id = request.GET.get('periodo')
    periodos = PeriodoSemestral.objects.all()
    periodo_sel = None

    if periodo_id:
        periodo_sel = get_object_or_404(PeriodoSemestral, pk=periodo_id)
        calificaciones = Calificacion.objects.filter(
            estudiante=estudiante,
            grupo__periodo=periodo_sel
        ).select_related('grupo__materia', 'grupo__profesor', 'grupo__periodo')
    else:
        calificaciones = Calificacion.objects.filter(
            estudiante=estudiante
        ).select_related('grupo__materia', 'grupo__profesor', 'grupo__periodo')

    # Promedio general
    promedio = None
    if calificaciones.exists():
        total = sum(float(c.calificacion) for c in calificaciones)
        promedio = round(total / calificaciones.count(), 2)

    return render(request, 'calificaciones/boleta.html', {
        'estudiante': estudiante,
        'calificaciones': calificaciones,
        'periodos': periodos,
        'periodo_sel': periodo_sel,
        'promedio': promedio,
    })

def boleta_print(request, pk):
    """Vista de impresión — sin base.html, abre en ventana nueva."""
    estudiante = get_object_or_404(Estudiante, pk=pk)
    periodo_id = request.GET.get('periodo')
    periodos = PeriodoSemestral.objects.all()
    periodo_sel = None

    if periodo_id:
        periodo_sel = get_object_or_404(PeriodoSemestral, pk=periodo_id)
        calificaciones = Calificacion.objects.filter(
            estudiante=estudiante,
            grupo__periodo=periodo_sel
        ).select_related('grupo__materia', 'grupo__profesor', 'grupo__periodo')
    else:
        calificaciones = Calificacion.objects.filter(
            estudiante=estudiante
        ).select_related('grupo__materia', 'grupo__profesor', 'grupo__periodo')

    promedio = None
    if calificaciones.exists():
        total = sum(float(c.calificacion) for c in calificaciones)
        promedio = round(total / calificaciones.count(), 2)

    return render(request, 'calificaciones/boleta_print.html', {
        'estudiante': estudiante,
        'calificaciones': calificaciones,
        'periodos': periodos,
        'periodo_sel': periodo_sel,
        'promedio': promedio,
    })


# ─── REPORTE DE CALIFICACIONES POR GRUPO ────────────────────────────────────

def reporte_calificaciones(request):
    """Reporte tipo lista de alumnos con calificación, por grupo."""
    grupos = Grupo.objects.select_related('materia', 'profesor', 'periodo').all()
    grupo_sel = None
    calificaciones = []
    sin_calificacion = []

    grupo_id = request.GET.get('grupo')
    if grupo_id:
        grupo_sel = get_object_or_404(Grupo, pk=grupo_id)
        # Estudiantes del grupo
        estudiantes_grupo = grupo_sel.estudiantes.all().order_by('apellidos', 'nombre')
        cals_dict = {c.estudiante_id: c for c in
                     Calificacion.objects.filter(grupo=grupo_sel).select_related('estudiante')}
        for est in estudiantes_grupo:
            if est.id in cals_dict:
                calificaciones.append(cals_dict[est.id])
            else:
                sin_calificacion.append(est)

    return render(request, 'calificaciones/reporte.html', {
        'grupos': grupos,
        'grupo_sel': grupo_sel,
        'calificaciones': calificaciones,
        'sin_calificacion': sin_calificacion,
    })


def reporte_print(request, pk):
    """Versión imprimible del reporte de calificaciones."""
    grupo = get_object_or_404(Grupo, pk=pk)
    estudiantes_grupo = grupo.estudiantes.all().order_by('apellidos', 'nombre')
    cals_dict = {c.estudiante_id: c for c in
                 Calificacion.objects.filter(grupo=grupo).select_related('estudiante')}
    filas = []
    for est in estudiantes_grupo:
        filas.append({
            'estudiante': est,
            'calificacion': cals_dict.get(est.id, None)
        })
    aprobados = sum(1 for f in filas if f['calificacion'] and f['calificacion'].calificacion >= 6)
    return render(request, 'calificaciones/reporte_print.html', {
        'grupo': grupo,
        'filas': filas,
        'aprobados': aprobados,
        'reprobados': len(filas) - aprobados,
    })


# ─── LISTA DE ALUMNOS POR AULA ───────────────────────────────────────────────

def aula_alumnos(request, pk):
    """Muestra los grupos asignados a un aula y sus estudiantes."""
    aula = get_object_or_404(Aula, pk=pk)
    periodo_id = request.GET.get('periodo')
    periodos = PeriodoSemestral.objects.all()
    periodo_sel = None

    grupos_qs = Grupo.objects.filter(aula=aula).select_related('materia', 'profesor', 'periodo', 'horario')
    if periodo_id:
        periodo_sel = get_object_or_404(PeriodoSemestral, pk=periodo_id)
        grupos_qs = grupos_qs.filter(periodo=periodo_sel)

    grupos_data = []
    for g in grupos_qs:
        grupos_data.append({
            'grupo': g,
            'estudiantes': g.estudiantes.all().order_by('apellidos', 'nombre'),
        })

    return render(request, 'aulas/alumnos.html', {
        'aula': aula,
        'grupos_data': grupos_data,
        'periodos': periodos,
        'periodo_sel': periodo_sel,
    })


def aula_alumnos_print(request, pk):
    """Versión imprimible de lista de alumnos por aula."""
    aula = get_object_or_404(Aula, pk=pk)
    periodo_id = request.GET.get('periodo')
    periodo_sel = None
    grupos_qs = Grupo.objects.filter(aula=aula).select_related('materia', 'profesor', 'periodo', 'horario')
    if periodo_id:
        periodo_sel = get_object_or_404(PeriodoSemestral, pk=periodo_id)
        grupos_qs = grupos_qs.filter(periodo=periodo_sel)

    grupos_data = []
    for g in grupos_qs:
        grupos_data.append({
            'grupo': g,
            'estudiantes': g.estudiantes.all().order_by('apellidos', 'nombre'),
        })

    return render(request, 'aulas/alumnos_print.html', {
        'aula': aula,
        'grupos_data': grupos_data,
        'periodo_sel': periodo_sel,
    })
