from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from rest_framework import viewsets
from .models import (
    Cirugia,
    Cita,
    Consulta,
    Dueno,
    Especialidad,
    Facturacion,
    Hospitalizacion,
    Mascota,
    Tratamiento,
    Veterinario,
)
from .serializers import (
    CirugiaSerializer,
    CitaSerializer,
    ConsultaSerializer,
    DuenoSerializer,
    EspecialidadSerializer,
    FacturacionSerializer,
    HospitalizacionSerializer,
    MascotaSerializer,
    TratamientoSerializer,
    VeterinarioSerializer,
)
from .forms import (
    MascotaForm,
    CitaForm,
    ReporteForm,
    DuenoForm,
    CirugiaForm,
    ConsultaForm,
    EspecialidadForm,
    FacturacionForm,
    HospitalizacionForm,
    TratamientoForm,
    VeterinarioForm,
)
from django.utils import timezone
from io import BytesIO
from .utils import render_pdf
from datetime import datetime


# ViewSets para API (ya existentes)
class CirugiaViewSet(viewsets.ModelViewSet):
    queryset = Cirugia.objects.all()
    serializer_class = CirugiaSerializer


class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer


class DuenoViewSet(viewsets.ModelViewSet):
    queryset = Dueno.objects.all()
    serializer_class = DuenoSerializer


class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer


class FacturacionViewSet(viewsets.ModelViewSet):
    queryset = Facturacion.objects.all()
    serializer_class = FacturacionSerializer


class HospitalizacionViewSet(viewsets.ModelViewSet):
    queryset = Hospitalizacion.objects.all()
    serializer_class = HospitalizacionSerializer


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer


class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer


class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer


# Funciones CRUD para Mascota (ya existentes)
def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, "mascota/lista_mascotas.html", {"mascotas": mascotas})


def crear_mascota(request):
    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():
            mascota = form.save(commit=False)
            # Aquí asignamos un dueño por defecto; ajusta la lógica según necesites.
            mascota.id_dueno = Dueno.objects.get(pk=1)
            mascota.save()
            return redirect("lista_mascotas")
    else:
        form = MascotaForm()
    return render(request, "mascota/crear_mascota.html", {"form": form})


def editar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == "POST":
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect("lista_mascotas")
    else:
        form = MascotaForm(instance=mascota)
    return render(request, "mascota/editar_mascota.html", {"form": form})


def eliminar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == "POST":
        mascota.delete()
        return redirect("lista_mascotas")
    return render(request, "mascota/eliminar_mascota.html", {"mascota": mascota})


# Funciones CRUD para Cita (ya existentes)
def lista_citas(request):
    citas = Cita.objects.select_related("id_mascota", "id_dueno").all()
    return render(request, "cita/lista_citas.html", {"citas": citas})


def crear_cita(request):
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_citas")
    else:
        form = CitaForm()
    return render(request, "cita/crear_cita.html", {"form": form})


def editar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == "POST":
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect("lista_citas")
    else:
        form = CitaForm(instance=cita)
    return render(request, "cita/editar_cita.html", {"form": form})


def eliminar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == "POST":
        cita.delete()
        return redirect("lista_citas")
    return render(request, "cita/eliminar_cita.html", {"cita": cita})


# Funciones CRUD para Cirugía
def lista_cirugias(request):
    cirugias = Cirugia.objects.select_related("id_mascota", "id_veterinario").all()
    return render(request, "cirugia/lista_cirugias.html", {"cirugias": cirugias})


def crear_cirugia(request):
    if request.method == "POST":
        form = CirugiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_cirugias")
    else:
        form = CirugiaForm()
    return render(request, "cirugia/crear_cirugia.html", {"form": form})


def editar_cirugia(request, pk):
    cirugia = get_object_or_404(Cirugia, pk=pk)
    if request.method == "POST":
        form = CirugiaForm(request.POST, instance=cirugia)
        if form.is_valid():
            form.save()
            return redirect("lista_cirugias")
    else:
        form = CirugiaForm(instance=cirugia)
    return render(request, "cirugia/editar_cirugia.html", {"form": form})


def eliminar_cirugia(request, pk):
    cirugia = get_object_or_404(Cirugia, pk=pk)
    if request.method == "POST":
        cirugia.delete()
        return redirect("lista_cirugias")
    return render(request, "cirugia/eliminar_cirugia.html", {"cirugia": cirugia})


# Funciones CRUD para Consulta
def lista_consultas(request):
    consultas = Consulta.objects.select_related("id_cita", "id_veterinario").all()
    return render(request, "consulta/lista_consultas.html", {"consultas": consultas})


def crear_consulta(request):
    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_consultas")
    else:
        form = ConsultaForm()
    return render(request, "consulta/crear_consulta.html", {"form": form})


def editar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == "POST":
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("lista_consultas")
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, "consulta/editar_consulta.html", {"form": form})


def eliminar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("lista_consultas")
    return render(request, "consulta/eliminar_consulta.html", {"consulta": consulta})


# Funciones CRUD para Dueño
def lista_duenos(request):
    duenos = Dueno.objects.all()
    return render(request, "dueno/lista_duenos.html", {"duenos": duenos})


def crear_dueno(request):
    if request.method == "POST":
        form = DuenoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_duenos")
    else:
        form = DuenoForm()
    return render(request, "dueno/crear_dueno.html", {"form": form})


def editar_dueno(request, pk):
    dueno = get_object_or_404(Dueno, pk=pk)
    if request.method == "POST":
        form = DuenoForm(request.POST, instance=dueno)
        if form.is_valid():
            form.save()
            return redirect("lista_duenos")
    else:
        form = DuenoForm(instance=dueno)
    return render(request, "dueno/editar_dueno.html", {"form": form})


def eliminar_dueno(request, pk):
    dueno = get_object_or_404(Dueno, pk=pk)
    if request.method == "POST":
        dueno.delete()
        return redirect("lista_duenos")
    return render(request, "dueno/eliminar_dueno.html", {"dueno": dueno})


# Funciones CRUD para Especialidad
def lista_especialidades(request):
    especialidades = Especialidad.objects.all()
    return render(
        request,
        "especialidad/lista_especialidades.html",
        {"especialidades": especialidades},
    )


def crear_especialidad(request):
    if request.method == "POST":
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_especialidades")
    else:
        form = EspecialidadForm()
    return render(request, "especialidad/crear_especialidad.html", {"form": form})


def editar_especialidad(request, pk):
    especialidad = get_object_or_404(Especialidad, pk=pk)
    if request.method == "POST":
        form = EspecialidadForm(request.POST, instance=especialidad)
        if form.is_valid():
            form.save()
            return redirect("lista_especialidades")
    else:
        form = EspecialidadForm(instance=especialidad)
    return render(request, "especialidad/editar_especialidad.html", {"form": form})


def eliminar_especialidad(request, pk):
    especialidad = get_object_or_404(Especialidad, pk=pk)
    if request.method == "POST":
        especialidad.delete()
        return redirect("lista_especialidades")
    return render(
        request,
        "especialidad/eliminar_especialidad.html",
        {"especialidad": especialidad},
    )


# Funciones CRUD para Facturación
def lista_facturaciones(request):
    facturaciones = Facturacion.objects.select_related("id_cita", "id_dueno").all()
    return render(
        request,
        "facturacion/lista_facturaciones.html",
        {"facturaciones": facturaciones},
    )


def crear_facturacion(request):
    if request.method == "POST":
        form = FacturacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_facturaciones")
    else:
        form = FacturacionForm()
    return render(request, "facturacion/crear_facturacion.html", {"form": form})


def editar_facturacion(request, pk):
    facturacion = get_object_or_404(Facturacion, pk=pk)
    if request.method == "POST":
        form = FacturacionForm(request.POST, instance=facturacion)
        if form.is_valid():
            form.save()
            return redirect("lista_facturaciones")
    else:
        form = FacturacionForm(instance=facturacion)
    return render(request, "facturacion/editar_facturacion.html", {"form": form})


def eliminar_facturacion(request, pk):
    facturacion = get_object_or_404(Facturacion, pk=pk)
    if request.method == "POST":
        facturacion.delete()
        return redirect("lista_facturaciones")
    return render(
        request, "facturacion/eliminar_facturacion.html", {"facturacion": facturacion}
    )


# Funciones CRUD para Hospitalización
def lista_hospitalizaciones(request):
    hospitalizaciones = Hospitalizacion.objects.select_related(
        "id_mascota", "id_veterinario"
    ).all()
    return render(
        request,
        "hospitalizacion/lista_hospitalizaciones.html",
        {"hospitalizaciones": hospitalizaciones},
    )


def crear_hospitalizacion(request):
    if request.method == "POST":
        form = HospitalizacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_hospitalizaciones")
    else:
        form = HospitalizacionForm()
    return render(request, "hospitalizacion/crear_hospitalizacion.html", {"form": form})


def editar_hospitalizacion(request, pk):
    hospitalizacion = get_object_or_404(Hospitalizacion, pk=pk)
    if request.method == "POST":
        form = HospitalizacionForm(request.POST, instance=hospitalizacion)
        if form.is_valid():
            form.save()
            return redirect("lista_hospitalizaciones")
    else:
        form = HospitalizacionForm(instance=hospitalizacion)
    return render(
        request, "hospitalizacion/editar_hospitalizacion.html", {"form": form}
    )


def eliminar_hospitalizacion(request, pk):
    hospitalizacion = get_object_or_404(Hospitalizacion, pk=pk)
    if request.method == "POST":
        hospitalizacion.delete()
        return redirect("lista_hospitalizaciones")
    return render(
        request,
        "hospitalizacion/eliminar_hospitalizacion.html",
        {"hospitalizacion": hospitalizacion},
    )


# Funciones CRUD para Tratamiento
def lista_tratamientos(request):
    tratamientos = Tratamiento.objects.select_related("id_mascota").all()
    return render(
        request, "tratamiento/lista_tratamientos.html", {"tratamientos": tratamientos}
    )


def crear_tratamiento(request):
    if request.method == "POST":
        form = TratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_tratamientos")
    else:
        form = TratamientoForm()
    return render(request, "tratamiento/crear_tratamiento.html", {"form": form})


def editar_tratamiento(request, pk):
    tratamiento = get_object_or_404(Tratamiento, pk=pk)
    if request.method == "POST":
        form = TratamientoForm(request.POST, instance=tratamiento)
        if form.is_valid():
            form.save()
            return redirect("lista_tratamientos")
    else:
        form = TratamientoForm(instance=tratamiento)
    return render(request, "tratamiento/editar_tratamiento.html", {"form": form})


def eliminar_tratamiento(request, pk):
    tratamiento = get_object_or_404(Tratamiento, pk=pk)
    if request.method == "POST":
        tratamiento.delete()
        return redirect("lista_tratamientos")
    return render(
        request, "tratamiento/eliminar_tratamiento.html", {"tratamiento": tratamiento}
    )


# Funciones CRUD para Veterinario
def lista_veterinarios(request):
    veterinarios = Veterinario.objects.select_related("id_especialidad").all()
    return render(
        request, "veterinario/lista_veterinarios.html", {"veterinarios": veterinarios}
    )


def crear_veterinario(request):
    if request.method == "POST":
        form = VeterinarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_veterinarios")
    else:
        form = VeterinarioForm()
    return render(request, "veterinario/crear_veterinario.html", {"form": form})


def editar_veterinario(request, pk):
    veterinario = get_object_or_404(Veterinario, pk=pk)
    if request.method == "POST":
        form = VeterinarioForm(request.POST, instance=veterinario)
        if form.is_valid():
            form.save()
            return redirect("lista_veterinarios")
    else:
        form = VeterinarioForm(instance=veterinario)
    return render(request, "veterinario/editar_veterinario.html", {"form": form})


def eliminar_veterinario(request, pk):
    veterinario = get_object_or_404(Veterinario, pk=pk)
    if request.method == "POST":
        veterinario.delete()
        return redirect("lista_veterinarios")
    return render(
        request, "veterinario/eliminar_veterinario.html", {"veterinario": veterinario}
    )


# Funciones de reportes (ya existentes)
def generar_reporte_citas(request):
    citas = Cita.objects.select_related("id_mascota", "id_dueno", "id_veterinario")
    template = get_template("reportes/reporte_citas.html")
    fecha_reporte = timezone.localtime(timezone.now()).strftime("%d/%m/%Y %H:%M:%S")
    generado_por = "Administrador"
    context = {
        "citas": citas,
        "fecha_reporte": fecha_reporte,
        "generado_por": generado_por,
    }
    html = template.render(context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'inline; filename="reporte_citas.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Ocurrió un error al generar el PDF", status=500)
    return response


def generar_reporte(request):
    template = get_template("reporte.html")
    if request.method == "POST":
        form = ReporteForm(request.POST)
        if form.is_valid():
            fecha_inicio = form.cleaned_data["fecha_inicio"]
            fecha_fin = form.cleaned_data["fecha_fin"]
            tipo_mascota = form.cleaned_data["tipo_mascota"]
            if tipo_mascota:
                mascotas = Mascota.objects.filter(especie=tipo_mascota)
            else:
                mascotas = Mascota.objects.all()
            context = {
                "mascotas": mascotas,
                "fecha_inicio": fecha_inicio,
                "fecha_fin": fecha_fin,
                "tipo_mascota": tipo_mascota,
            }
            html = template.render(context)
            response = HttpResponse(content_type="application/pdf")
            response["Content-Disposition"] = (
                f'inline; filename="reporte-{tipo_mascota}-{fecha_inicio}.pdf"'
            )
            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse("Ocurrió un error al generar el PDF", status=500)
            return response
    else:
        form = ReporteForm()
    return render(request, "reporte_form.html", {"form": form})


def home(request):
    return render(request, "home.html")
