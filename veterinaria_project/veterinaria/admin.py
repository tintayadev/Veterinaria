from django.http import HttpResponse
from django.utils import timezone
import io
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.units import inch


from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.cache import cache
from django.contrib.admin import AdminSite

from .models import Cirugia, Cita, Consulta, Dueno, Especialidad, Facturacion, Hospitalizacion, Mascota, Tratamiento, Veterinario

class EdadFilter(admin.SimpleListFilter):
    title = 'Edad'
    parameter_name = 'edad'

    def lookups(self, request, model_admin):
        return (
            ('0-1', 'Menos de 1 año'),
            ('1-5', '1-5 años'),
            ('5+', 'Más de 5 años'),
        )

    def queryset(self, request, queryset):
        if self.value() == '0-1':
            return queryset.filter(fechanacimiento__gte=timezone.now().date() - timezone.timedelta(days=365))
        elif self.value() == '1-5':
            return queryset.filter(fechanacimiento__gte=timezone.now().date() - timezone.timedelta(days=365*5),
                                   fechanacimiento__lt=timezone.now().date() - timezone.timedelta(days=365))
        elif self.value() == '5+':
            return queryset.filter(fechanacimiento__lt=timezone.now().date() - timezone.timedelta(days=365*5))

@admin.register(Cirugia)
class CirugiaAdmin(admin.ModelAdmin):
    list_display = ('id_cirugia', 'fecha_formatted', 'tipo', 'descripcion', 'view_mascota_link', 'view_veterinario_link')
    list_filter = ('fecha', 'tipo')
    search_fields = ('id_cirugia', 'tipo', 'id_mascota__nombre', 'id_veterinario__nombre')

    def fecha_formatted(self, obj):
        return obj.fecha.strftime("%d/%m/%Y")
    fecha_formatted.short_description = "Fecha"

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
    list_display = ('id_cita', 'fecha_formatted', 'hora', 'motivo', 'view_consulta_link')
    list_filter = ('fecha', 'id_veterinario')
    search_fields = ('id_cita', 'motivo', 'id_mascota__nombre', 'id_dueno__nombre', 'id_veterinario__nombre')

    def fecha_formatted(self, obj):
        return obj.fecha.strftime("%d/%m/%Y")
    fecha_formatted.short_description = "Fecha"

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
    list_display = ('id_consulta', 'fecha_formatted', 'hora', 'diagnostico', 'observaciones', 'view_cita_link')
    list_filter = ('fecha', 'id_veterinario')
    search_fields = ('id_consulta', 'diagnostico', 'id_cita__id', 'id_veterinario__nombre')

    def fecha_formatted(self, obj):
        return obj.fecha.strftime("%d/%m/%Y")
    fecha_formatted.short_description = "Fecha"

    def view_cita_link(self, obj):
        url = reverse("admin:veterinaria_cita_change", args=[obj.id_cita.pk])
        return format_html('<a href="{}">Ver Cita</a>', url)
    view_cita_link.short_description = "Cita"

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


@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('id_especialidad', 'nombre', 'descripcion')
    search_fields = ('id_especialidad', 'nombre', 'descripcion')

@admin.register(Facturacion)
class FacturacionAdmin(admin.ModelAdmin):
    list_display = ('id_factura', 'fecha_formatted', 'id_dueno', 'total', 'pagado', 'view_cita_link')
    list_filter = ('fecha', 'pagado')
    search_fields = ('id_factura', 'id_cita__id', 'id_dueno__nombre')
    actions = ['mark_as_paid']

    def fecha_formatted(self, obj):
        return obj.fecha.strftime("%d/%m/%Y")
    fecha_formatted.short_description = "Fecha"

    def view_cita_link(self, obj):
        url = reverse("admin:veterinaria_cita_change", args=[obj.id_cita.pk])
        return format_html('<a href="{}">Ver Cita</a>', url)
    view_cita_link.short_description = "Cita"

    def mark_as_paid(self, request, queryset):
        queryset.update(pagado=True)
        self.message_user(request, "Facturas marcadas como pagadas.")
    mark_as_paid.short_description = "Marcar como pagado"

    # actions = ['export_as_pdf']

    # def export_as_pdf(self, request, queryset):
    #     response = HttpResponse(content_type='application/pdf')
    #     response['Content-Disposition'] = f'attachment; filename=facturas-{timezone.now().strftime("%Y-%m-%d")}.pdf'

    #     buffer = io.BytesIO()
    #     doc = SimpleDocTemplate(buffer, pagesize=A4)
    #     elements = []

    #     styles = getSampleStyleSheet()
    #     styles.add(ParagraphStyle(name='Center', alignment=1))

    #     for factura in queryset:
    #         elements.append(Paragraph("Factura", styles['Title']))
    #         elements.append(Spacer(1, 0.25*inch))

    #         # Información de la factura
    #         elements.append(Paragraph(f"Número de Factura: {factura.id_factura}", styles['Normal']))
    #         elements.append(Paragraph(f"Fecha: {factura.fecha.strftime('%d/%m/%Y')}", styles['Normal']))
    #         elements.append(Paragraph(f"Cliente: {factura.id_dueno.nombre} {factura.id_dueno.apellidos}", styles['Normal']))
    #         elements.append(Spacer(1, 0.25*inch))

    #         # Detalles de la factura
    #         data = [['Descripción', 'Cantidad', 'Precio Unitario', 'Total']]
    #         # Aquí deberías iterar sobre los items de la factura
    #         # Por ejemplo, si tienes una relación con los items:
    #         # for item in factura.items.all():
    #         #     data.append([item.descripcion, str(item.cantidad), f"${item.precio_unitario}", f"${item.total}"])
            
    #         # Como no tenemos esa información, vamos a agregar una fila de ejemplo
    #         data.append(['Consulta veterinaria', '1', '$50.00', '$50.00'])

    #         table = Table(data)
    #         style = TableStyle([
    #             ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    #             ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    #             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #             ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    #             ('FONTSIZE', (0, 0), (-1, 0), 12),
    #             ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    #             ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    #             ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
    #             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #             ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    #             ('FONTSIZE', (0, 1), (-1, -1), 10),
    #             ('TOPPADDING', (0, 1), (-1, -1), 6),
    #             ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    #             ('GRID', (0, 0), (-1, -1), 1, colors.black)
    #         ])
    #         table.setStyle(style)
    #         elements.append(table)

    #         elements.append(Spacer(1, 0.25*inch))
    #         elements.append(Paragraph(f"Total: ${factura.total}", styles['Normal']))
    #         elements.append(Paragraph(f"Estado: {'Pagado' if factura.pagado else 'Pendiente'}", styles['Normal']))

    #         elements.append(PageBreak())

    #     doc.build(elements)

    #     pdf = buffer.getvalue()
    #     buffer.close()
    #     response.write(pdf)

    #     return response

    # export_as_pdf.short_description = "Exportar seleccionados como PDF"

@admin.register(Hospitalizacion)
class HospitalizacionAdmin(admin.ModelAdmin):
    list_display = ('id_hospitalizacion', 'fechaingreso_formatted', 'fechaalta_formatted', 'motivo', 'view_mascota_link', 'view_veterinario_link')
    list_filter = ('fechaingreso', 'fechaalta')
    search_fields = ('id_hospitalizacion', 'motivo', 'id_mascota__nombre', 'id_veterinario__nombre')

    def fechaingreso_formatted(self, obj):
        return obj.fechaingreso.strftime("%d/%m/%Y")
    fechaingreso_formatted.short_description = "Fecha de Ingreso"

    def fechaalta_formatted(self, obj):
        return obj.fechaalta.strftime("%d/%m/%Y") if obj.fechaalta else "No dado de alta"
    fechaalta_formatted.short_description = "Fecha de Alta"

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
    list_display = ('id_mascota', 'nombre', 'raza', 'especie', 'edad', 'peso', 'sexo', 'fechanacimiento', 'edad_calculada', 'view_dueno_link')
    list_filter = ('especie', 'sexo', 'edad', EdadFilter)
    search_fields = ('id_mascota', 'nombre', 'raza', 'especie', 'id_dueno__nombre')
    readonly_fields = ('edad_calculada',)

    def edad_calculada(self, obj):
        if obj.fechanacimiento:
            return (timezone.now().date() - obj.fechanacimiento).days // 365
        return "Desconocida"
    edad_calculada.short_description = "Edad Calculada"

    def view_dueno_link(self, obj):
        url = reverse("admin:veterinaria_dueno_change", args=[obj.id_dueno.pk])
        return format_html('<a href="{}">Ver Dueño</a>', url)
    view_dueno_link.short_description = "Dueño"

    # actions = ['export_as_pdf']

    # def export_as_pdf(self, request, queryset):
    #     response = HttpResponse(content_type='application/pdf')
    #     response['Content-Disposition'] = f'attachment; filename=mascotas-{timezone.now().strftime("%Y-%m-%d")}.pdf'

    #     buffer = io.BytesIO()
    #     doc = SimpleDocTemplate(buffer, pagesize=letter)
    #     elements = []

    #     # Título
    #     styles = getSampleStyleSheet()
    #     elements.append(Paragraph("Reporte de Mascotas", styles['Title']))

    #     # Datos de la tabla
    #     data = [['Nombre', 'Especie', 'Raza', 'Edad', 'Dueño']]
    #     for mascota in queryset:
    #         data.append([
    #             mascota.nombre,
    #             mascota.especie,
    #             mascota.raza,
    #             str(mascota.edad),
    #             f"{mascota.id_dueno.nombre} {mascota.id_dueno.apellidos}" if mascota.id_dueno else "Sin dueño"
    #         ])

    #     # Crear la tabla
    #     table = Table(data)
    #     style = TableStyle([
    #         ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    #         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    #         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    #         ('FONTSIZE', (0, 0), (-1, 0), 14),
    #         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    #         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    #         ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
    #         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #         ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    #         ('FONTSIZE', (0, 1), (-1, -1), 12),
    #         ('TOPPADDING', (0, 1), (-1, -1), 6),
    #         ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    #         ('GRID', (0, 0), (-1, -1), 1, colors.black)
    #     ])
    #     table.setStyle(style)
    #     elements.append(table)

    #     # Construir el PDF
    #     doc.build(elements)

    #     pdf = buffer.getvalue()
    #     buffer.close()
    #     response.write(pdf)

    #     return response

    # export_as_pdf.short_description = "Exportar seleccionados como PDF"

@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
    list_display = ('id_tratamiento', 'descripcion', 'dosis', 'duracion', 'fechainicio_formatted', 'fechafin_formatted', 'view_mascota_link')
    list_filter = ('fechainicio', 'fechafin')
    search_fields = ('id_tratamiento', 'descripcion', 'id_mascota__nombre')

    def fechainicio_formatted(self, obj):
        return obj.fechainicio.strftime("%d/%m/%Y")
    fechainicio_formatted.short_description = "Fecha de Inicio"

    def fechafin_formatted(self, obj):
        return obj.fechafin.strftime("%d/%m/%Y") if obj.fechafin else "En curso"
    fechafin_formatted.short_description = "Fecha de Fin"

    def view_mascota_link(self, obj):
        url = reverse("admin:veterinaria_mascota_change", args=[obj.id_mascota.pk])
        return format_html('<a href="{}">Ver Mascota</a>', url)
    view_mascota_link.short_description = "Mascota"

    def clean(self):
        if self.fechafin and self.fechainicio and self.fechafin < self.fechainicio:
            raise ValidationError("La fecha de fin no puede ser anterior a la fecha de inicio.")

@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('id_veterinario', 'nombre', 'apellidos', 'especialidad', 'telefono', 'email')
    search_fields = ('id_veterinario', 'nombre', 'apellidos', 'especialidad__nombre', 'telefono', 'email')
    #filter_horizontal = ('especialidades',)  # Asumiendo que tienes una relación many-to-many con Especialidad

    def especialidad(self, obj):
        return obj.id_especialidad.nombre
    especialidad.short_description = 'Especialidad'

class MyAdminSite(AdminSite):
    def index(self, request, extra_context=None):
        # Cachear para evitar consultas frecuentes
        mascota_count = cache.get('mascota_count')
        if not mascota_count:
            mascota_count = Mascota.objects.count()
            cache.set('mascota_count', mascota_count, 3600)  # Cache por 1 hora

        extra_context = extra_context or {}
        extra_context['mascota_count'] = mascota_count
        return super().index(request, extra_context)

admin.site.site_header = 'Administración de Veterinaria Huellitas'
admin.site.site_title = 'Veterinaria Huellitas'