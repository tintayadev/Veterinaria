from rest_framework import serializers
from .models import Cirugia, Cita, Consulta, Dueno, Especialidad, Facturacion, Hospitalizacion, Mascota, Tratamiento, Veterinario

from rest_framework import serializers
from .models import Cirugia, Cita, Consulta, Dueno, Especialidad, Facturacion, Hospitalizacion, Mascota, Tratamiento, Veterinario

class CirugiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cirugia
        fields = '__all__'  # Incluye todos los campos del modelo Cirugia

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'  # Incluye todos los campos del modelo Cita

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'  # Incluye todos los campos del modelo Consulta

class DuenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dueno
        fields = '__all__'  # Incluye todos los campos del modelo Dueno

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'  # Incluye todos los campos del modelo Especialidad

class FacturacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facturacion
        fields = '__all__'  # Incluye todos los campos del modelo Facturacion

class HospitalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospitalizacion
        fields = '__all__'  # Incluye todos los campos del modelo Hospitalizacion

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'  # Incluye todos los campos del modelo Mascota

class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = '__all__'  # Incluye todos los campos del modelo Tratamiento

class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = '__all__'  # Incluye todos los campos del modelo Veterinario
