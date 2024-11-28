from django import forms
from .models import Mascota, Cita
from django.utils import timezone

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'raza', 'especie', 'edad']

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha', 'hora', 'id_mascota', 'id_dueno', 'motivo']


class ReporteForm(forms.Form):
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    # Obtener todas las especies únicas de las mascotas
    especies = Mascota.objects.values('especie').distinct()

    # Crear la lista de opciones para el campo tipo_mascota
    tipo_mascota_choices = [(especie['especie'], especie['especie']) for especie in especies]

    # Agregar la opción por defecto (vacía)
    tipo_mascota_choices.insert(0, ('', 'Seleccione una especie'))

    tipo_mascota = forms.ChoiceField(
        required=False,
        choices=tipo_mascota_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
