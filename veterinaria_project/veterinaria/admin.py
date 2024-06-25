from django.contrib import admin
from .models import Cirugia, Cita, Consulta, Dueno, Especialidad, Facturacion, Hospitalizacion, Mascota, Tratamiento, Veterinario


# from django.contrib.admin import AdminSite
# from django.utils.translation import gettext_lazy as _

# class CustomAdminSite(AdminSite):
#     site_header = _('Administración de Veterinaria U')
#     site_title = _('Veterinaria U')
#     index_title = _('Bienvenido al panel de administración')

#     def each_context(self, request):
#         context = super().each_context(request)
#         context['custom_admin_css'] = 'admin/css/custom_admin.css'
#         return context

# admin_site = CustomAdminSite(name='custom_admin')

@admin.register(Cirugia)
class CirugiaAdmin(admin.ModelAdmin):
    list_display = ('id_cirugia', 'fecha', 'tipo', 'descripcion')
    list_filter = ('fecha', 'tipo')
    search_fields = ('id_cirugia', 'tipo', 'id_mascota__nombre', 'id_veterinario__nombre')

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('id_cita', 'fecha', 'hora', 'id_mascota', 'id_dueno', 'id_veterinario', 'motivo')
    list_filter = ('fecha', 'id_veterinario')
    search_fields = ('id_cita', 'motivo', 'id_mascota__nombre', 'id_dueno__nombre', 'id_veterinario__nombre')

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id_consulta', 'fecha', 'hora', 'id_cita', 'id_veterinario', 'diagnostico', 'observaciones')
    list_filter = ('fecha', 'id_veterinario')
    search_fields = ('id_consulta', 'diagnostico', 'id_cita__id', 'id_veterinario__nombre')

@admin.register(Dueno)
class DuenoAdmin(admin.ModelAdmin):
    list_display = ('id_dueno', 'nombre', 'apellidos', 'telefono', 'direccion', 'email')
    search_fields = ('id_dueno', 'nombre', 'apellidos', 'telefono', 'direccion', 'email')

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('id_especialidad', 'nombre', 'descripcion')
    search_fields = ('id_especialidad', 'nombre', 'descripcion')

@admin.register(Facturacion)
class FacturacionAdmin(admin.ModelAdmin):
    list_display = ('id_factura', 'fecha', 'id_cita', 'id_dueno', 'total', 'pagado')
    list_filter = ('fecha', 'pagado')
    search_fields = ('id_factura', 'id_cita__id', 'id_dueno__nombre')

@admin.register(Hospitalizacion)
class HospitalizacionAdmin(admin.ModelAdmin):
    list_display = ('id_hospitalizacion', 'fechaingreso', 'fechaalta', 'motivo', 'id_mascota', 'id_veterinario')
    list_filter = ('fechaingreso', 'fechaalta')
    search_fields = ('id_hospitalizacion', 'motivo', 'id_mascota__nombre', 'id_veterinario__nombre')

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('id_mascota', 'nombre', 'raza', 'especie', 'edad', 'peso', 'sexo', 'fechanacimiento', 'id_dueno')
    list_filter = ('especie', 'sexo', 'edad')
    search_fields = ('id_mascota', 'nombre', 'raza', 'especie', 'id_dueno__nombre')

@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
    list_display = ('id_tratamiento', 'descripcion', 'dosis', 'duracion', 'fechainicio', 'fechafin', 'id_mascota')
    list_filter = ('fechainicio', 'fechafin')
    search_fields = ('id_tratamiento', 'descripcion', 'id_mascota__nombre')


admin.site.site_header = 'Administración de Veterinaria Huellitas'
admin.site.site_title = 'Veterinaria Huellitas'