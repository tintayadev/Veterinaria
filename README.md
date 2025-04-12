# Proyecto Veterinaria Huellitas

Este es un sistema web desarrollado con **Django** y **PostgreSQL** para la gestión integral de una veterinaria. La aplicación permite administrar cirugías, citas, consultas, dueños, especialidades, facturación, hospitalización, mascotas, tratamientos y veterinarios.

## Requisitos

- Docker
- Docker Compose

## Ejecución Rápida

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/tintayadev/Veterinaria
   cd Veterinaria
   ```

2. Construir y levantar el proyecto:

   ```bash
   docker compose up --build
   ```

   Esto iniciará los siguientes servicios:

   - **db:** Base de datos PostgreSQL.
   - **backend:** Aplicación Django, que ejecuta automáticamente `makemigrations` y `migrate` antes de levantar el servidor en `0.0.0.0:8000`.
   - **adminer:** Interfaz web para la gestión de PostgreSQL en `http://localhost:8080`.

3. Acceder a la aplicación:

   - Página principal: [http://localhost:8000](http://localhost:8000)
   - Panel de administración de Django: [http://localhost:8000/admin](http://localhost:8000/admin)
   - Adminer: [http://localhost:8080](http://localhost:8080)

## Carga de Datos Iniciales (Fixtures)

Para poblar la base de datos con datos de ejemplo, se ha incluido un fixture en formato JSON:

1. Coloca el archivo `initial_data.json` en la carpeta `backend/veterinaria/fixtures/`.
2. Ejecuta el siguiente comando:

   ```bash
   docker compose exec backend python manage.py loaddata initial_data.json
   ```

## Docker Compose

El archivo `docker-compose.yml` define los servicios necesarios junto con su configuración. Los comentarios explican cada línea:

```yaml
version: "3.9"

services:
  db:
    # Usa la imagen de PostgreSQL 15
    image: postgres:15
    # Reinicia el contenedor siempre que falle
    restart: always
    # Configuración de variables de entorno para la base de datos, tomadas de .env
    environment:
      POSTGRES_DB: ${POSTGRES_DB} # Nombre de la base de datos
      POSTGRES_USER: ${POSTGRES_USER} # Usuario de la base de datos
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD} # Contraseña de la base de datos
    volumes:
      # Monta un volumen para persistir los datos de PostgreSQL
      - postgres_data:/var/lib/postgresql/data
    ports:
      # Expone el puerto 5432 en el host para conectar a la base de datos
      - "5432:5432"

  backend:
    # Construye la imagen a partir del directorio ./backend
    build:
      context: ./backend
    # Lee variables de entorno desde el archivo .env
    env_file: .env
    # Depende del servicio de la base de datos (db)
    depends_on:
      - db
    # Ejecuta estos comandos al iniciar el contenedor:
    # 1. Makemigrations y migrate para aplicar las migraciones de Django
    # 2. Levanta el servidor de desarrollo de Django en 0.0.0.0:8000
    command: >
      sh -c "
        python manage.py makemigrations &&
        python manage.py migrate &&
        python manage.py runserver 0.0.0.0:8000
      "
    volumes:
      # Monta el directorio de código para reflejar en tiempo real los cambios
      - ./backend:/app
    ports:
      # Expone el puerto 8000 en el host para acceder a la aplicación
      - "8000:8000"

  adminer:
    # Usa la imagen de Adminer para la administración de la base de datos
    image: adminer
    restart: always
    ports:
      # Expone el puerto 8080 en el host para acceder a Adminer
      - "8080:8080"

volumes:
  # Define un volumen para persistir los datos de PostgreSQL
  postgres_data:
```

## Dockerfile para el Backend

El archivo `backend/Dockerfile` contiene las instrucciones para construir la imagen del servicio backend. Cada línea se explica a continuación:

```dockerfile
# Usa una imagen base slim de Python 3.11
FROM python:3.11-slim

# Evita que Python escriba archivos .pyc y asegura salida sin búfer (ideal para logs)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos al directorio de trabajo
COPY requirements.txt .
# Actualiza pip e instala las dependencias listadas en requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto del código fuente al contenedor
COPY . .
```

## Comandos Útiles con Docker

Ejecutar comandos de Django desde el contenedor `backend`:

- **Crear superusuario:**

  ```bash
  docker compose exec backend python manage.py createsuperuser
  ```

- **Revisar el estado de las migraciones:**

  ```bash
  docker compose exec backend python manage.py showmigrations
  ```

- **Aplicar migraciones manualmente (si es necesario):**

  ```bash
  docker compose exec backend python manage.py migrate
  ```

- **Acceder al shell de Django:**

  ```bash
  docker compose exec backend python manage.py shell
  ```

- **Acceder a la base de datos PostgreSQL:**

  ```bash
  docker compose exec db psql -U postgres -d veterinaria
  ```

- **Ver logs de los servicios:**

  ```bash
  docker compose logs -f backend
  docker compose logs -f db
  ```

- **Detener los servicios:**

  ```bash
  docker compose down
  ```

- **Eliminar todos los volúmenes (para reiniciar la base de datos desde cero):**

  ```bash
  docker compose down -v
  ```

## Estructura del Proyecto

- `backend/`: Código fuente de la aplicación Django.
  - `veterinaria/`: Contiene los archivos de la aplicación, entre ellos:
    - `models.py`: Definiciones de modelos.
    - `forms.py`: Formularios para cada modelo, incluyendo ChoiceFields personalizados para mostrar nombres legibles.
    - `views.py`: Vistas CRUD y funcionalidades adicionales (como generación de reportes).
    - `urls.py`: Rutas de la API y de las vistas tradicionales.
    - `fixtures/`: Archivos JSON para cargar datos iniciales (por ejemplo, `initial_data.json`).
    - `templates/`: Plantillas organizadas en carpetas por módulo (mascota, cita, dueno, cirugia, consulta, especialidad, facturacion, hospitalizacion, tratamiento, veterinario) y la plantilla principal `home.html`.
- `postgres-init/`: Archivos de inicialización opcional para PostgreSQL.
- `.env`: Variables de entorno para configuración.
- `docker-compose.yml`: Archivo de orquestación de servicios.
- `docs/`: Documentación técnica y guía de usuario.

## Documentación

- [Guía de Usuario](docs/guia_usuario.md)
- [Documentación Técnica](docs/doc_tecnica.md)

