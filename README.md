# Proyecto Veterinaria Huellitas

Este es un sistema web desarrollado con **Django** y **PostgreSQL** para la gestión integral de una veterinaria. Permite administrar cirugías, citas, consultas, dueños, especialidades, facturación, hospitalización, mascotas, tratamientos y veterinarios.

## Requisitos

- Docker
- Docker Compose

## Ejecución rápida

1. Clonar el repositorio:

```bash
git clone https://github.com/tintayadev/Veterinaria
cd Veterinaria
```

2. Construir y levantar el proyecto:

```bash
docker compose up --build
```

Esto iniciará la base de datos y el backend de Django, aplicando las migraciones necesarias de forma automática. Una vez iniciado, el sistema estará disponible en:

- `http://localhost:8000` (página principal)
- `http://localhost:8000/admin` (panel de administración)

## Comandos útiles con Docker

Ejecutar comandos de Django desde el contenedor `backend`:

- Crear superusuario:

```bash
docker compose exec backend python manage.py createsuperuser
```

- Revisar el estado de las migraciones:

```bash
docker compose exec backend python manage.py showmigrations
```

- Aplicar migraciones manualmente (si fuera necesario):

```bash
docker compose exec backend python manage.py migrate
```

- Acceder al shell de Django:

```bash
docker compose exec backend python manage.py shell
```

- Acceder a la base de datos PostgreSQL:

```bash
docker compose exec db psql -U postgres -d veterinaria
```

- Ver logs de los servicios:

```bash
docker compose logs -f backend
docker compose logs -f db
```

- Detener los servicios:

```bash
docker compose down
```

- Eliminar todos los volúmenes (para reiniciar la base de datos desde cero):

```bash
docker compose down -v
```

## Estructura del Proyecto

- `backend/`: Código fuente de la aplicación Django.
- `postgres-init/`: Archivos de inicialización opcional para PostgreSQL.
- `.env`: Variables de entorno para configuración.
- `docker-compose.yml`: Archivo de orquestación de servicios.
- `docs/`: Documentación técnica y guía de usuario.

## Documentación

- [Guía de Usuario](docs/guia_usuario.md)
- [Documentación Técnica](docs/doc_tecnica.md)

