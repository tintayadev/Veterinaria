
from django.db import models

class Cirugia(models.Model):
    id_cirugia = models.AutoField(primary_key=True, db_column='ID_Cirugia')
    fecha = models.DateField(db_column='Fecha')
    tipo = models.CharField(max_length=50, db_column='Tipo')
    descripcion = models.CharField(max_length=250, blank=True, null=True, db_column='Descripcion')
    id_mascota = models.ForeignKey('Mascota', on_delete=models.DO_NOTHING, db_column='ID_Mascota')
    id_veterinario = models.ForeignKey('Veterinario', on_delete=models.DO_NOTHING, db_column='ID_Veterinario')

    class Meta:
        db_table = 'Cirugia'

class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True, db_column='ID_Cita')
    fecha = models.DateField(db_column='Fecha')
    hora = models.TimeField(db_column='Hora')
    id_mascota = models.ForeignKey('Mascota', on_delete=models.DO_NOTHING, db_column='ID_Mascota')
    id_dueno = models.ForeignKey('Dueno', on_delete=models.DO_NOTHING, db_column='ID_Dueno')
    id_veterinario = models.ForeignKey('Veterinario', on_delete=models.DO_NOTHING, db_column='ID_Veterinario')
    motivo = models.CharField(max_length=100, blank=True, null=True, db_column='Motivo')

    class Meta:
        db_table = 'Cita'

class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True, db_column='ID_Consulta')
    fecha = models.DateField(db_column='Fecha')
    hora = models.TimeField(db_column='Hora')
    diagnostico = models.CharField(max_length=200, blank=True, null=True, db_column='Diagnostico')
    observaciones = models.TextField(blank=True, null=True, db_column='Observaciones')
    id_cita = models.ForeignKey(Cita, on_delete=models.DO_NOTHING, db_column='ID_Cita')
    id_veterinario = models.ForeignKey('Veterinario', on_delete=models.DO_NOTHING, db_column='ID_Veterinario')

    class Meta:
        db_table = 'Consulta'

class Dueno(models.Model):
    id_dueno = models.AutoField(primary_key=True, db_column='ID_Dueno')
    nombre = models.CharField(max_length=50, db_column='Nombre')
    apellidos = models.CharField(max_length=50, db_column='Apellidos')
    telefono = models.CharField(max_length=20, blank=True, null=True, db_column='Telefono')
    direccion = models.CharField(max_length=100, blank=True, null=True, db_column='Direccion')
    email = models.CharField(max_length=50, blank=True, null=True, db_column='Email')

    class Meta:
        db_table = 'Dueno'

class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True, db_column='ID_Especialidad')
    nombre = models.CharField(max_length=50, db_column='Nombre')
    descripcion = models.CharField(max_length=200, blank=True, null=True, db_column='Descripcion')

    class Meta:
        db_table = 'Especialidad'

class Facturacion(models.Model):
    id_factura = models.AutoField(primary_key=True, db_column='ID_Factura')
    fecha = models.DateField(db_column='Fecha')
    id_cita = models.ForeignKey(Cita, on_delete=models.DO_NOTHING, db_column='ID_Cita')
    id_dueno = models.ForeignKey(Dueno, on_delete=models.DO_NOTHING, db_column='ID_Dueno')
    total = models.DecimalField(max_digits=10, decimal_places=2, db_column='Total')
    pagado = models.BooleanField(default=False, db_column='Pagado')

    class Meta:
        db_table = 'Facturacion'

class Hospitalizacion(models.Model):
    id_hospitalizacion = models.AutoField(primary_key=True, db_column='ID_Hospitalizacion')
    fechaingreso = models.DateField(db_column='FechaIngreso')
    fechaalta = models.DateField(blank=True, null=True, db_column='FechaAlta')
    motivo = models.CharField(max_length=200, blank=True, null=True, db_column='Motivo')
    id_mascota = models.ForeignKey('Mascota', on_delete=models.DO_NOTHING, db_column='ID_Mascota')
    id_veterinario = models.ForeignKey('Veterinario', on_delete=models.DO_NOTHING, db_column='ID_Veterinario')

    class Meta:
        db_table = 'Hospitalizacion'

class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True, db_column='ID_Mascota')
    nombre = models.CharField(max_length=50, db_column='Nombre')
    raza = models.CharField(max_length=50, blank=True, null=True, db_column='Raza')
    especie = models.CharField(max_length=50, db_column='Especie')
    edad = models.IntegerField(blank=True, null=True, db_column='Edad')
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, db_column='Peso')
    sexo = models.CharField(max_length=1, blank=True, null=True, db_column='Sexo')
    fechanacimiento = models.DateField(blank=True, null=True, db_column='FechaNacimiento')
    id_dueno = models.ForeignKey(Dueno, on_delete=models.DO_NOTHING, db_column='ID_Dueno')

    class Meta:
        db_table = 'Mascota'

class Tratamiento(models.Model):
    id_tratamiento = models.AutoField(primary_key=True, db_column='ID_Tratamiento')
    descripcion = models.CharField(max_length=200, db_column='Descripcion')
    dosis = models.CharField(max_length=50, blank=True, null=True, db_column='Dosis')
    duracion = models.CharField(max_length=50, blank=True, null=True, db_column='Duracion')
    fechainicio = models.DateField(blank=True, null=True, db_column='FechaInicio')
    fechafin = models.DateField(blank=True, null=True, db_column='FechaFin')
    id_mascota = models.ForeignKey(Mascota, on_delete=models.DO_NOTHING, db_column='ID_Mascota')

    class Meta:
        db_table = 'Tratamiento'

class Veterinario(models.Model):
    id_veterinario = models.AutoField(primary_key=True, db_column='ID_Veterinario')
    nombre = models.CharField(max_length=50, db_column='Nombre')
    apellidos = models.CharField(max_length=50, db_column='Apellidos')
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.DO_NOTHING, db_column='ID_Especialidad')
    telefono = models.CharField(max_length=20, blank=True, null=True, db_column='Telefono')
    email = models.CharField(max_length=50, blank=True, null=True, db_column='Email')

    class Meta:
        db_table = 'Veterinario'
