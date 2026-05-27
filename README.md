# Sistema Web de Control Escolar
### Django + Bootstrap 5 + PostgreSQL

---

## 📋 Requisitos previos
- Python 3.10+
- PostgreSQL 14+
- pip

---

## 🗄️ 1. Configurar PostgreSQL

Abre pgAdmin o la terminal de PostgreSQL y ejecuta:

```sql
-- Crear la base de datos
CREATE DATABASE control_escolar_db;

-- (Opcional) Crear un usuario dedicado
CREATE USER escolar_user WITH PASSWORD 'tu_password_segura';
GRANT ALL PRIVILEGES ON DATABASE control_escolar_db TO escolar_user;
```

Luego edita `control_escolar/settings.py` con tus datos:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'control_escolar_db',
        'USER': 'postgres',        # o escolar_user
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## ⚙️ 2. Instalación del proyecto

```bash
# 1. Crear entorno virtual
python -m venv env

# 2. Activar entorno virtual
# Windows:
env\Scripts\activate
# Mac/Linux:
source env/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Crear las tablas en PostgreSQL (migraciones)
python manage.py makemigrations
python manage.py migrate

# 5. Crear superusuario para el panel admin
python manage.py createsuperuser

# 6. Ejecutar el servidor
python manage.py runserver
```

Visita: **http://127.0.0.1:8000/**
Panel admin: **http://127.0.0.1:8000/admin/**

---

## 📁 Estructura del proyecto

```
control_escolar/
├── control_escolar/        # Configuración del proyecto
│   ├── settings.py         # ← Configura tu BD aquí
│   ├── urls.py
│   └── wsgi.py
├── escolar/                # App principal
│   ├── models.py           # 9 modelos / entidades
│   ├── views.py            # Vistas CRUD para cada módulo
│   ├── forms.py            # Formularios
│   ├── urls.py             # Rutas URL
│   ├── admin.py            # Panel admin
│   └── templates/          # Plantillas HTML
│       ├── base.html       # Plantilla base con navbar
│       ├── home.html       # Dashboard
│       ├── carreras/
│       ├── profesores/
│       ├── estudiantes/
│       ├── materias/
│       ├── aulas/
│       ├── periodos/
│       ├── horarios/
│       ├── grupos/
│       └── calificaciones/
├── manage.py
└── requirements.txt
```

---

## 🗺️ Módulos y URLs

| Módulo             | URL base            |
|--------------------|---------------------|
| Inicio / Dashboard | `/`                 |
| Carreras           | `/carreras/`        |
| Profesores         | `/profesores/`      |
| Estudiantes        | `/estudiantes/`     |
| Materias           | `/materias/`        |
| Aulas              | `/aulas/`           |
| Periodos           | `/periodos/`        |
| Horarios           | `/horarios/`        |
| Grupos             | `/grupos/`          |
| Calificaciones     | `/calificaciones/`  |

---

## 📊 Tablas creadas en PostgreSQL

Después de `python manage.py migrate`, se crean automáticamente:

| Tabla Django            | Descripción                          |
|-------------------------|--------------------------------------|
| `escolar_carrera`       | Carreras de la institución           |
| `escolar_profesor`      | Datos de los profesores              |
| `escolar_estudiante`    | Alumnos relacionados a una carrera   |
| `escolar_materia`       | Materias con clave y créditos        |
| `escolar_aula`          | Aulas con capacidad y ubicación      |
| `escolar_periodosemestral` | Periodos académicos              |
| `escolar_horario`       | Horarios por día y hora              |
| `escolar_grupo`         | Grupos (profesor + materia + aula…)  |
| `escolar_grupo_estudiantes` | Relación M2M grupo↔estudiante   |
| `escolar_calificacion`  | Calificaciones por estudiante/grupo  |

---

## 🚀 Despliegue en Render (hosting gratuito)

1. Sube el proyecto a GitHub.
2. En `settings.py` agrega `dj-database-url` y configura la BD desde la variable de entorno `DATABASE_URL`.
3. Instala `gunicorn` y `whitenoise`.
4. Crea un servicio Web en render.com apuntando a tu repo.
5. Agrega la variable de entorno `DATABASE_URL` de tu PostgreSQL en Render.
