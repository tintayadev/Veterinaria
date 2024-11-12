from django import forms
from .models import Mascota, Cita

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'raza', 'especie', 'edad']

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha', 'hora', 'id_mascota', 'id_dueno', 'motivo']
