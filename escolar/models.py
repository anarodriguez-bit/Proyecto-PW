from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Carrera(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre de la carrera')
    clave = models.CharField(max_length=20, unique=True, verbose_name='Clave')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')

    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.clave} - {self.nombre}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre(s)')
    apellidos = models.CharField(max_length=100, verbose_name='Apellidos')
    email = models.EmailField(unique=True, verbose_name='Correo electrónico')
    telefono = models.CharField(max_length=15, blank=True, verbose_name='Teléfono')
    especialidad = models.CharField(max_length=150, blank=True, verbose_name='Especialidad')
    numero_empleado = models.CharField(max_length=20, unique=True, verbose_name='No. Empleado')

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = ['apellidos', 'nombre']

    def __str__(self):
        return f"{self.apellidos}, {self.nombre}"

    def nombre_completo(self):
        return f"{self.nombre} {self.apellidos}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre(s)')
    apellidos = models.CharField(max_length=100, verbose_name='Apellidos')
    matricula = models.CharField(max_length=20, unique=True, verbose_name='Matrícula')
    email = models.EmailField(unique=True, verbose_name='Correo electrónico')
    telefono = models.CharField(max_length=15, blank=True, verbose_name='Teléfono')
    carrera = models.ForeignKey(Carrera, on_delete=models.PROTECT, verbose_name='Carrera')
    fecha_ingreso = models.DateField(verbose_name='Fecha de ingreso')

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering = ['apellidos', 'nombre']

    def __str__(self):
        return f"{self.matricula} - {self.apellidos}, {self.nombre}"

    def nombre_completo(self):
        return f"{self.nombre} {self.apellidos}"


class Materia(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre de la materia')
    clave = models.CharField(max_length=20, unique=True, verbose_name='Clave')
    creditos = models.PositiveSmallIntegerField(verbose_name='Créditos')
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, verbose_name='Carrera')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        ordering = ['carrera', 'nombre']

    def __str__(self):
        return f"{self.clave} - {self.nombre}"


class Aula(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre/Número de aula')
    capacidad = models.PositiveSmallIntegerField(verbose_name='Capacidad (alumnos)')
    ubicacion = models.CharField(max_length=150, verbose_name='Ubicación / Edificio')

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} (Cap: {self.capacidad})"


class PeriodoSemestral(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre del periodo',
                               help_text='Ej: Enero-Junio 2026')
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio')
    fecha_fin = models.DateField(verbose_name='Fecha de fin')
    activo = models.BooleanField(default=False, verbose_name='Periodo activo')

    class Meta:
        verbose_name = 'Periodo Semestral'
        verbose_name_plural = 'Periodos Semestrales'
        ordering = ['-fecha_inicio']

    def __str__(self):
        return self.nombre


class Horario(models.Model):
    DIAS_SEMANA = [
        ('LUN', 'Lunes'),
        ('MAR', 'Martes'),
        ('MIE', 'Miércoles'),
        ('JUE', 'Jueves'),
        ('VIE', 'Viernes'),
        ('SAB', 'Sábado'),
    ]
    dia = models.CharField(max_length=3, choices=DIAS_SEMANA, verbose_name='Día')
    hora_inicio = models.TimeField(verbose_name='Hora de inicio')
    hora_fin = models.TimeField(verbose_name='Hora de fin')

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering = ['dia', 'hora_inicio']

    def __str__(self):
        return f"{self.get_dia_display()} {self.hora_inicio.strftime('%H:%M')} - {self.hora_fin.strftime('%H:%M')}"


class Grupo(models.Model):
    nombre = models.CharField(max_length=10, verbose_name='Nombre/Clave del grupo',
                               help_text='Ej: A, B, G1, G2')
    profesor = models.ForeignKey(Profesor, on_delete=models.PROTECT, verbose_name='Profesor')
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT, verbose_name='Materia')
    aula = models.ForeignKey(Aula, on_delete=models.PROTECT, verbose_name='Aula')
    periodo = models.ForeignKey(PeriodoSemestral, on_delete=models.PROTECT, verbose_name='Periodo semestral')
    horario = models.ForeignKey(Horario, on_delete=models.PROTECT, verbose_name='Horario')
    estudiantes = models.ManyToManyField(Estudiante, blank=True, verbose_name='Estudiantes inscritos')

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        ordering = ['periodo', 'materia', 'nombre']

    def __str__(self):
        return f"Grupo {self.nombre} - {self.materia} ({self.periodo})"


class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name='Estudiante')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name='Grupo')
    calificacion = models.DecimalField(
        max_digits=4, decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name='Calificación'
    )
    observaciones = models.TextField(blank=True, verbose_name='Observaciones')

    class Meta:
        verbose_name = 'Calificación'
        verbose_name_plural = 'Calificaciones'
        unique_together = ('estudiante', 'grupo')
        ordering = ['grupo', 'estudiante']

    def __str__(self):
        return f"{self.estudiante.nombre_completo()} | {self.grupo} | {self.calificacion}"
