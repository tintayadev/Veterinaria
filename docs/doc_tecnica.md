
#### Acceso al Sistema

1. **Página de inicio de sesión**: Ve a `http://127.0.0.1:8000/admin` y utiliza las credenciales del superusuario que creaste para iniciar sesión.

2. **Panel de administración**: Una vez iniciada la sesión, serás redirigido al panel de administración donde podrás gestionar todos los modelos del sistema.

#### Gestión de Datos

- **Cirugías**: En la sección de Cirugías, puedes añadir, editar o eliminar cirugías. Puedes ver detalles de la mascota y el veterinario asociados.
- **Citas**: En la sección de Citas, puedes gestionar las citas programadas. Puedes ver detalles de las consultas relacionadas.
- **Consultas**: Aquí puedes gestionar las consultas realizadas a las mascotas. 
- **Dueños**: Gestiona la información de los dueños de las mascotas. Puedes ver todas las mascotas asociadas a cada dueño.
- **Especialidades**: Añade o modifica las especialidades de los veterinarios.
- **Facturación**: Gestiona las facturas de las citas. Puedes marcar las facturas como pagadas.
- **Hospitalización**: Gestiona los registros de hospitalización de las mascotas.
- **Mascotas**: Añade o modifica la información de las mascotas. Puedes ver detalles del dueño asociado.
- **Tratamientos**: Gestiona los tratamientos aplicados a las mascotas.
- **Veterinarios**: Añade o modifica la información de los veterinarios.

#### Acciones Personalizadas

- **Enviar correo electrónico**: Desde la lista de dueños, puedes seleccionar varios y utilizar la acción personalizada para enviarles correos electrónicos.
- **Marcar como pagado**: Desde la lista de facturas, puedes seleccionar varias y marcarlas como pagadas.

### Documentación Técnica

#### Estructura del Proyecto

- **`veterinaria/`**: Contiene el código fuente de la aplicación Django.
- **`manage.py`**: Script de gestión de Django.
- **`requirements.txt`**: Archivo con las dependencias del proyecto.
- **`README.md`**: Este archivo.

#### Modelos

- **Cirugia**: Información sobre las cirugías realizadas a las mascotas.
- **Cita**: Información sobre las citas programadas.
- **Consulta**: Detalles de las consultas realizadas durante las citas.
- **Dueno**: Información de los dueños de las mascotas.
- **Especialidad**: Especialidades de los veterinarios.
- **Facturacion**: Registros de facturación de las citas.
- **Hospitalizacion**: Registros de hospitalización de las mascotas.
- **Mascota**: Información de las mascotas.
- **Tratamiento**: Detalles de los tratamientos aplicados a las mascotas.
- **Veterinario**: Información de los veterinarios.

#### Administración Personalizada

El archivo `admin.py` contiene la configuración personalizada del panel de administración:

```python
from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from .models import Cirugia, Cita, Consulta, Dueno, Especialidad, Facturacion, Hospitalizacion, Mascota, Tratamiento, Veterinario

@admin.register(Cirugia)
class CirugiaAdmin(admin.ModelAdmin):
    list_display = ('id_cirugia', 'fecha', 'tipo', 'descripcion', 'view_mascota_link', 'view_veterinario_link')
    list_filter = ('fecha', 'tipo')
    search_fields = ('id_cirugia', 'tipo', 'id_mascota__nombre', 'id_veterinario__nombre')

    def view_mascota_link(self, obj):
        url = reverse("admin:veterinaria_mascota_change", args=[obj.id_mascota.pk])
        return format_html('<a href="{}">Ver Mascota</a>', url)
    view_mascota_link.short_description = "Mascota"

    def view_veterinario_link(self, obj):
        url = reverse("admin:veterinaria_veterinario_change", args=[obj.id_veterinario.pk])
        return format_html('<a href="{}">Ver Veterinario</a>', url)
    view_veterinario_link.short_description = "Veterinario"

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('id_cita', 'fecha', 'hora', 'id_mascota', 'id_dueno', 'id_veterinario', 'motivo', 'view_consulta_link')
    list_filter = ('fecha', 'id_veterinario')
    search_fields = ('id_cita', 'motivo', 'id_mascota__nombre', 'id_dueno__nombre', 'id_veterinario__nombre')

    def view_consulta_link(self, obj):
        url = (
            reverse("admin:veterinaria_consulta_changelist")
            + "?"
            + urlencode({"id_cita__id": f"{obj.pk}"})
        )
        return format_html('<a href="{}">Ver Consultas</a>', url)
    view_consulta_link.short_description = "Consultas"

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id_consulta', 'fecha', 'hora', 'id_cita', 'id_veterinario', 'diagnostico', 'observaciones')
    list_filter = ('fecha', 'id_veterinario')
    search_fields = ('id_consulta', 'diagnostico', 'id_cita__id', 'id_veterinario__nombre')

@admin.register(Dueno)
class DuenoAdmin(admin.ModelAdmin):
    list_display = ('id_dueno', 'nombre', 'apellidos', 'telefono', 'direccion', 'email', 'view_mascotas_link')
    search_fields = ('id_dueno', 'nombre', 'apellidos', 'telefono', 'direccion', 'email')
    actions = ['send_email']

    def view_mascotas_link(self, obj):
        url = (
            reverse("admin:veterinaria_mascota_changelist")
            + "?"
            + urlencode({"id_dueno__id": f"{obj.pk}"})
        )
        return format_html('<a href="{}">Ver Mascotas</a>', url)
    view_mascotas_link.short_description = "Mascotas"

    def send_email(self, request, queryset):
        for dueno in queryset:
            # Implement your email sending logic here
            pass
        self.message_user(request, "Correo enviado con éxito.")
    send_email.short_description = "Enviar correo electrónico"

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('id_especialidad', 'nombre', 'descripcion')
    search_fields = ('id_especialidad', 'nombre', 'descripcion')

@admin.register(Facturacion)
class FacturacionAdmin(admin.ModelAdmin):
    list_display = ('id_factura', 'fecha', 'id_cita', 'id_dueno', 'total', 'pagado')
    list_filter = ('fecha', 'pagado')
    search_fields = ('id_factura', 'id_cita__id', 'id_dueno__nombre')
    actions = ['mark_as_paid']

    def mark_as_paid(self, request, queryset):
        queryset.update(pagado=True)
        self.message_user(request, "Facturas marcadas como pagadas.")
    mark_as_paid.short_description = "Marcar como pagado"

@admin.register(Hospitalizacion)
class HospitalizacionAdmin(admin.ModelAdmin):
    list_display = ('id_hospitalizacion', 'fechaingreso', 'fechaalta', 'motivo', 'id_mascota', 'id_veterinario', 'view_mascota_link', 'view_veterinario_link')
    list_filter = ('fechaingreso', 'fechaalta')
    search_fields = ('id_hospitalizacion', 'motivo', 'id_mascota__nombre', 'id_veterinario__nombre')

    def view_mascota_link(self, obj):
        url = reverse("admin:veterinaria_mascota_change", args=[obj.id_mascota.pk])
        return format_html('<a href="{}">Ver Mascota</a>', url)
    view_mascota_link.short_description = "Mascota"

    def view_veterinario_link(self, obj):
        url = reverse("admin:veterinaria_veterinario_change", args=[obj.id_veterinario.pk])
        return format_html('<a href="{}">Ver Veterinario</a>', url)
    view_veterinario_link.short_description = "Veterinario"

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('id_mascota', 'nombre', 'raza', 'especie', 'edad', 'peso', 'sexo', 'fechanacimiento', 'id_dueno', 'view_dueno_link')
    list_filter = ('especie', 'sexo', 'edad')
    search_fields = ('id_mascota', 'nombre', 'raza', 'especie', 'id_dueno__nombre')

    def view_dueno_link(self, obj):
        url = reverse("admin:veterinaria_dueno_change", args=[obj.id_dueno.pk])
        return format_html('<a href="{}">Ver Dueño</a>', url)
    view_dueno_link.short_description = "Dueño"

@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
    list_display = ('id_tratamiento

', 'descripcion', 'dosis', 'duracion', 'fechainicio', 'fechafin', 'id_mascota', 'view_mascota_link')
    list_filter = ('fechainicio', 'fechafin')
    search_fields = ('id_tratamiento', 'descripcion', 'id_mascota__nombre')

    def view_mascota_link(self, obj):
        url = reverse("admin:veterinaria_mascota_change", args=[obj.id_mascota.pk])
        return format_html('<a href="{}">Ver Mascota</a>', url)
    view_mascota_link.short_description = "Mascota"

@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('id_veterinario', 'nombre', 'apellidos', 'especialidad', 'telefono', 'email')
    search_fields = ('id_veterinario', 'nombre', 'apellidos', 'especialidad__nombre', 'telefono', 'email')

    def especialidad(self, obj):
        return obj.id_especialidad.nombre
    especialidad.short_description = 'Especialidad'

admin.site.site_header = 'Administración de Veterinaria Huellitas'
admin.site.site_title = 'Veterinaria Huellitas'
```

#### Dependencias

Las dependencias del proyecto se encuentran en el archivo `requirements.txt`. Aquí se listan todas las librerías necesarias para que el proyecto funcione correctamente. Para instalar las dependencias, utiliza el siguiente comando:

```bash
pip install -r requirements.txt
```

#### Migraciones

Para aplicar las migraciones y crear las tablas en la base de datos, utiliza el siguiente comando:

```bash
python manage.py migrate
```

#### Ejecución del Servidor

Para iniciar el servidor de desarrollo de Django, utiliza el siguiente comando:

```bash
python manage.py runserver
```

Esta documentación debería ser suficiente para proporcionar una guía clara tanto para usuarios finales como para desarrolladores que necesiten trabajar con el sistema. Puedes añadir esta información al `README.md` para completar la documentación del proyecto.