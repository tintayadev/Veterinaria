from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from rest_framework import viewsets
from .models import Cirugia, Cita, Consulta, Dueno, Especialidad, Facturacion, Hospitalizacion, Mascota, Tratamiento, Veterinario
from .serializers import (CirugiaSerializer, CitaSerializer, ConsultaSerializer, DuenoSerializer,
                          EspecialidadSerializer, FacturacionSerializer, HospitalizacionSerializer,
                          MascotaSerializer, TratamientoSerializer, VeterinarioSerializer)
from .forms import CitaForm, MascotaForm, ReporteForm
from django.utils import timezone
from io import BytesIO
from .utils import render_pdf
from datetime import datetime

# ViewSet para el modelo Cirugia
class CirugiaViewSet(viewsets.ModelViewSet):
    queryset = Cirugia.objects.all()
    serializer_class = CirugiaSerializer

# ViewSet para el modelo Cita
class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

# ViewSet para el modelo Consulta
class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

# ViewSet para el modelo Dueno
class DuenoViewSet(viewsets.ModelViewSet):
    queryset = Dueno.objects.all()
    serializer_class = DuenoSerializer

# ViewSet para el modelo Especialidad
class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

# ViewSet para el modelo Facturacion
class FacturacionViewSet(viewsets.ModelViewSet):
    queryset = Facturacion.objects.all()
    serializer_class = FacturacionSerializer

# ViewSet para el modelo Hospitalizacion
class HospitalizacionViewSet(viewsets.ModelViewSet):
    queryset = Hospitalizacion.objects.all()
    serializer_class = HospitalizacionSerializer

# ViewSet para el modelo Mascota
class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

# ViewSet para el modelo Tratamiento
class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

# ViewSet para el modelo Veterinario
class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer


# Vista para listar todas las mascotas
def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascota/lista_mascotas.html', {'mascotas': mascotas})

# Vista para crear una nueva mascota
def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'mascota/crear_mascota.html', {'form': form})

# Vista para editar una mascota existente
def editar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'mascota/editar_mascota.html', {'form': form})

# Vista para eliminar una mascota
def eliminar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect('lista_mascotas')
    return render(request, 'mascota/eliminar_mascota.html', {'mascota': mascota})

def lista_citas(request):
    citas = Cita.objects.select_related('id_mascota', 'id_dueno').all()
    return render(request, 'cita/lista_citas.html', {'citas': citas})

# Vista para crear una nueva cita
def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm()
    return render(request, 'cita/crear_cita.html', {'form': form})

# Vista para editar una cita existente
def editar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'cita/editar_cita.html', {'form': form})

# Vista para eliminar una mascota
def eliminar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('lista_citas')
    return render(request, 'cita/eliminar_cita.html', {'mascota': cita})

def home(request):
    return render(request, 'home.html')


def generar_reporte_citas(request):
    # Obtener datos de las citas
    citas = Cita.objects.select_related('id_mascota', 'id_dueno', 'id_veterinario')

    # Cargar el template HTML
    template = get_template('reportes/reporte_citas.html')

    # Obtener la fecha actual y el nombre del usuario (en este caso, simplemente un nombre estático)
    fecha_reporte = timezone.localtime(timezone.now()).strftime('%d/%m/%Y %H:%M:%S')

    generado_por = "Administrador"  # Puedes cambiar esto según el contexto de quien genera el reporte

    # Crear el contexto para el reporte
    context = {'citas': citas, 'fecha_reporte': fecha_reporte, 'generado_por': generado_por}

    # Renderizar el HTML con el contexto
    html = template.render(context)

    # Generar el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="reporte_citas.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Manejar errores
    if pisa_status.err:
        return HttpResponse('Ocurrió un error al generar el PDF', status=500)
    
    return response

def generar_reporte(request):
    template = get_template('reporte.html')
    if request.method == 'POST':
        form = ReporteForm(request.POST)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            tipo_mascota = form.cleaned_data['tipo_mascota']

            # Si se selecciona un tipo de mascota, filtrar por ese tipo
            if tipo_mascota:
                mascotas = Mascota.objects.filter(especie=tipo_mascota)
            else:
                mascotas = Mascota.objects.all()

            # Aquí pasamos los datos al template de reporte
            context = {
                'mascotas': mascotas,
                'fecha_inicio': fecha_inicio,
                'fecha_fin': fecha_fin,
                'tipo_mascota': tipo_mascota,
            }

            # Renderizar el HTML con el contexto
            html = template.render(context)

            # Generar el PDF
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename="reporte-{tipo_mascota}-{fecha_inicio}.pdf"'
            pisa_status = pisa.CreatePDF(html, dest=response)

            # Manejar errores
            if pisa_status.err:
                return HttpResponse('Ocurrió un error al generar el PDF', status=500)
            
            return response
            
    else:
        form = ReporteForm()

    return render(request, 'reporte_form.html', {'form': form})


from django.http import JsonResponse

def ping(request):
    return JsonResponse({"message": "pong"})
