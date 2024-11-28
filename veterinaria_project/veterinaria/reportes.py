# veterinaria/reportes.py
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse
import datetime

def render_pdf(data):
    # Lógica para renderizar el PDF
    html_string = render_to_string('reportes/reporte_mascotas.html', data)
    html = HTML(string=html_string)
    pdf = html.write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="reporte_mascotas_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf"'
    return response
