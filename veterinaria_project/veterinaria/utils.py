# veterinaria/utils.py

from io import BytesIO
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from django.utils import timezone
from datetime import datetime

def render_pdf(citas):
    # Crear un buffer en memoria
    buffer = BytesIO()

    # Crear un objeto canvas para generar el PDF
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter  # Tamaño de la página

    # Título del reporte
    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, height - 40, "Reporte de Citas")

    # Fecha y hora de generación
    p.setFont("Helvetica", 10)
    fecha_reporte = timezone.now().strftime("%d/%m/%Y %H:%M:%S")
    p.drawString(400, height - 60, f"Fecha del reporte: {fecha_reporte}")

    # Encabezados de la tabla
    p.setFont("Helvetica-Bold", 10)
    p.drawString(30, height - 100, "Fecha")
    p.drawString(150, height - 100, "Mascota")
    p.drawString(300, height - 100, "Tipo")
    p.drawString(450, height - 100, "Dueño")

    # Dibujar las citas en la tabla
    p.setFont("Helvetica", 10)
    y_position = height - 120  # Iniciar desde esta posición en el eje Y

    for cita in citas:
        p.drawString(30, y_position, cita.fecha.strftime("%d/%m/%Y %H:%M:%S"))
        p.drawString(150, y_position, cita.mascota.nombre)
        p.drawString(300, y_position, cita.mascota.tipo)
        p.drawString(450, y_position, cita.mascota.duenio)
        y_position -= 20

        # Verificar si el espacio se ha agotado para una nueva página
        if y_position < 100:
            p.showPage()
            p.setFont("Helvetica-Bold", 10)
            p.drawString(30, height - 100, "Fecha")
            p.drawString(150, height - 100, "Mascota")
            p.drawString(300, height - 100, "Tipo")
            p.drawString(450, height - 100, "Dueño")
            y_position = height - 120

    # Guardar el PDF generado
    p.showPage()
    p.save()

    # Mover el contenido del buffer a la respuesta HTTP
    buffer.seek(0)
    return buffer.getvalue()
