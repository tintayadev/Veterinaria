from django import forms
from .models import (
    Mascota,
    Cita,
    Dueno,
    Cirugia,
    Consulta,
    Especialidad,
    Facturacion,
    Hospitalizacion,
    Tratamiento,
    Veterinario,
)
from django.utils import timezone


class DuenoChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.nombre} {obj.apellidos}"


class VeterinarioChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.nombre} {obj.apellidos}"


class MascotaForm(forms.ModelForm):
    id_dueno = DuenoChoiceField(queryset=Dueno.objects.all())

    class Meta:
        model = Mascota
        fields = ["nombre", "raza", "especie", "edad", "id_dueno"]


class CitaForm(forms.ModelForm):
    id_dueno = DuenoChoiceField(queryset=Dueno.objects.all())
    id_veterinario = VeterinarioChoiceField(queryset=Veterinario.objects.all())

    class Meta:
        model = Cita
        fields = ["fecha", "hora", "id_mascota", "id_dueno", "id_veterinario", "motivo"]


class DuenoForm(forms.ModelForm):
    class Meta:
        model = Dueno
        fields = ["nombre", "apellidos", "telefono", "direccion", "email"]


class CirugiaForm(forms.ModelForm):
    id_veterinario = VeterinarioChoiceField(queryset=Veterinario.objects.all())

    class Meta:
        model = Cirugia
        fields = ["fecha", "tipo", "descripcion", "id_mascota", "id_veterinario"]


class ConsultaForm(forms.ModelForm):
    id_veterinario = VeterinarioChoiceField(queryset=Veterinario.objects.all())

    class Meta:
        model = Consulta
        fields = [
            "fecha",
            "hora",
            "diagnostico",
            "observaciones",
            "id_cita",
            "id_veterinario",
        ]


class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ["nombre", "descripcion"]


class FacturacionForm(forms.ModelForm):
    id_dueno = DuenoChoiceField(queryset=Dueno.objects.all())

    class Meta:
        model = Facturacion
        fields = ["fecha", "id_cita", "id_dueno", "total", "pagado"]


class HospitalizacionForm(forms.ModelForm):
    id_veterinario = VeterinarioChoiceField(queryset=Veterinario.objects.all())

    class Meta:
        model = Hospitalizacion
        fields = ["fechaingreso", "fechaalta", "motivo", "id_mascota", "id_veterinario"]


class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = [
            "descripcion",
            "dosis",
            "duracion",
            "fechainicio",
            "fechafin",
            "id_mascota",
        ]


class VeterinarioForm(forms.ModelForm):
    id_especialidad = forms.ModelChoiceField(queryset=Especialidad.objects.all())

    class Meta:
        model = Veterinario
        fields = ["nombre", "apellidos", "id_especialidad", "telefono", "email"]


class ReporteForm(forms.Form):
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    tipo_mascota = forms.ChoiceField(
        required=False, choices=[], widget=forms.Select(attrs={"class": "form-control"})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            especies = Mascota.objects.values_list("especie", flat=True).distinct()
            choices = [(especie, especie) for especie in especies]
            choices.insert(0, ("", "Seleccione una especie"))
            self.fields["tipo_mascota"].choices = choices
        except Exception:
            self.fields["tipo_mascota"].choices = [("", "Seleccione una especie")]
