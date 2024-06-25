# Proyecto Veterinaria Huellitas

Este es un proyecto Django para la gestión de una veterinaria, incluyendo administración de cirugías, citas, consultas, dueños, especialidades, facturación, hospitalización, mascotas, tratamientos y veterinarios.

## Requisitos

- Python 3.x
- pip
- virtualenv (opcional pero recomendado)

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tintayadev/Veterinaria
cd veterinaria_project
```

### 2. Crear y activar un entorno virtual (opcional pero recomendado)

```bash
# Crear un entorno virtual
python -m venv env

# Activar el entorno virtual
# En Windows
env\Scripts\activate
# En macOS/Linux
source env/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

Asegúrate de tener una base de datos configurada y de actualizar la configuración en `settings.py` según tus necesidades.

Ejecuta las migraciones para crear las tablas en la base de datos:

```bash
python manage.py migrate
```

### 5. Crear un superusuario

Crea un superusuario para acceder al panel de administración de Django:

```bash
python manage.py createsuperuser
```


### 6. Iniciar el servidor de desarrollo

Inicia el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

Accede al proyecto en tu navegador en `http://127.0.0.1:8000`.

## Uso

Para acceder al panel de administración, ve a `http://127.0.0.1:8000/admin` e inicia sesión con el superusuario que creaste anteriormente.

## Estructura del Proyecto

- `veterinaria_project/`: Contiene el código fuente de la aplicación Django.
- `manage.py`: Script de gestión de Django.
- `requirements.txt`: Archivo con las dependencias del proyecto.
- `README.md`: Este archivo.

## Contribuciones

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama nueva (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva característica'`).
4. Empuja tus cambios a la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

