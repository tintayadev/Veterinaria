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
    
    tipo_mascota = forms.ChoiceField(
        required=False,
        choices=[],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            especies = Mascota.objects.values_list('especie', flat=True).distinct()
            choices = [(especie, especie) for especie in especies]
            choices.insert(0, ('', 'Seleccione una especie'))
            self.fields['tipo_mascota'].choices = choices
        except Exception:
            # Si la tabla aún no existe, dejamos la lista vacía para evitar errores
            self.fields['tipo_mascota'].choices = [('', 'Seleccione una especie')]