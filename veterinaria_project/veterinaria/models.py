# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# class Cirugia(models.Model):
#     id_cirugia = models.AutoField(db_column='ID_Cirugia', primary_key=True, blank=True, null=False)  # Field name made lowercase.
#     fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
#     tipo = models.CharField(db_column='Tipo')  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion', blank=True, null=True, max_length=250)  # Field name made lowercase.
#     id_mascota = models.ForeignKey('Mascota', models.DO_NOTHING, db_column='ID_Mascota')  # Field name made lowercase.
#     id_veterinario = models.ForeignKey('Veterinario', models.DO_NOTHING, db_column='ID_Veterinario')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Cirugia'


# class Cita(models.Model):
#     id_cita = models.AutoField(db_column='ID_Cita', primary_key=True, blank=True, null=False)  # Field name made lowercase.
#     fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
#     hora = models.TimeField(db_column='Hora')  # Field name made lowercase.
#     id_mascota = models.ForeignKey('Mascota', models.DO_NOTHING, db_column='ID_Mascota')  # Field name made lowercase.
#     id_dueno = models.ForeignKey('Dueno', models.DO_NOTHING, db_column='ID_Dueno')  # Field name made lowercase.
#     id_veterinario = models.ForeignKey('Veterinario', models.DO_NOTHING, db_column='ID_Veterinario')  # Field name made lowercase.
#     motivo = models.CharField(db_column='Motivo', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Cita'


# class Consulta(models.Model):
#     id_consulta = models.AutoField(db_column='ID_Consulta', primary_key=True, blank=True, null=False)  # Field name made lowercase.
#     fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
#     hora = models.TimeField(db_column='Hora')  # Field name made lowercase.
#     diagnostico = models.CharField(db_column='Diagnostico', blank=True, null=True)  # Field name made lowercase.
#     observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
#     id_cita = models.ForeignKey(Cita, models.DO_NOTHING, db_column='ID_Cita')  # Field name made lowercase.
#     id_veterinario = models.ForeignKey('Veterinario', models.DO_NOTHING, db_column='ID_Veterinario')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Consulta'


# class Dueno(models.Model):
#     id_dueno = models.AutoField(db_column='ID_Dueno', primary_key=True, blank=True, null=False)  # Field name made lowercase.
#     nombre = models.CharField(db_column='Nombre')  # Field name made lowercase.
#     apellidos = models.CharField(db_column='Apellidos')  # Field name made lowercase.
#     telefono = models.CharField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.
#     direccion = models.CharField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='Email', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Dueno'


# class Especialidad(models.Model):
#     id_especialidad = models.AutoField(db_column='ID_Especialidad', primary_key=True, blank=True, null=False)  # Field name made lowercase.
#     nombre = models.CharField(db_column='Nombre')  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Especialidad'


# class Facturacion(models.Model):
#     id_factura = models.AutoField(db_column='ID_Factura', primary_key=True, blank=True, null=False)  # Field name made lowercase.
#     fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
#     id_cita = models.ForeignKey(Cita, models.DO_NOTHING, db_column='ID_Cita')  # Field name made lowercase.
#     id_dueno = models.ForeignKey(Dueno, models.DO_NOTHING, db_column='ID_Dueno')  # Field name made lowercase.
#     total = models.DecimalField(db_column='Total', max_digits=10, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
#     pagado = models.BooleanField(db_column='Pagado', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Facturacion'


# class Hospitalizacion(models.Model):
#     id_hospitalizacion = models.TextField(db_column='ID_Hospitalizacion', primary_key=True, blank=True, null=False)  # Field name made lowercase. This field type is a guess.
#     fechaingreso = models.DateField(db_column='FechaIngreso')  # Field name made lowercase.
#     fechaalta = models.DateField(db_column='FechaAlta', blank=True, null=True)  # Field name made lowercase.
#     motivo = models.CharField(db_column='Motivo', blank=True, null=True)  # Field name made lowercase.
#     id_mascota = models.ForeignKey('Mascota', models.DO_NOTHING, db_column='ID_Mascota')  # Field name made lowercase.
#     id_veterinario = models.ForeignKey('Veterinario', models.DO_NOTHING, db_column='ID_Veterinario')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Hospitalizacion'


# class Mascota(models.Model):
#     id_mascota = models.AutoField(db_column='ID_Mascota', primary_key=True, blank=True, null=False)  # Field name made lowercase.
#     nombre = models.CharField(db_column='Nombre')  # Field name made lowercase.
#     raza = models.CharField(db_column='Raza', blank=True, null=True)  # Field name made lowercase.
#     especie = models.CharField(db_column='Especie')  # Field name made lowercase.
#     edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
#     peso = models.DecimalField(db_column='Peso', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
#     sexo = models.CharField(db_column='Sexo', blank=True, null=True)  # Field name made lowercase.
#     fechanacimiento = models.DateField(db_column='FechaNacimiento', blank=True, null=True)  # Field name made lowercase.
#     id_dueno = models.ForeignKey(Dueno, models.DO_NOTHING, db_column='ID_Dueno')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Mascota'


# class Tratamiento(models.Model):
#     id_tratamiento = models.AutoField(db_column='ID_Tratamiento', primary_key=True, blank=True, null=False)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion')  # Field name made lowercase.
#     dosis = models.CharField(db_column='Dosis', blank=True, null=True)  # Field name made lowercase.
#     duracion = models.CharField(db_column='Duracion', blank=True, null=True)  # Field name made lowercase.
#     fechainicio = models.DateField(db_column='FechaInicio', blank=True, null=True)  # Field name made lowercase.
#     fechafin = models.DateField(db_column='FechaFin', blank=True, null=True)  # Field name made lowercase.
#     id_mascota = models.ForeignKey(Mascota, models.DO_NOTHING, db_column='ID_Mascota')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Tratamiento'


# class Veterinario(models.Model):
#     id_veterinario = models.AutoField(db_column='ID_Veterinario', primary_key=True, blank=True, null=False)  # Field name made lowercase.
#     nombre = models.CharField(db_column='Nombre')  # Field name made lowercase.
#     apellidos = models.CharField(db_column='Apellidos')  # Field name made lowercase.
#     id_especialidad = models.ForeignKey(Especialidad, models.DO_NOTHING, db_column='ID_Especialidad')  # Field name made lowercase.
#     telefono = models.CharField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='Email', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Veterinario'

from django.db import models

class Cirugia(models.Model):
    id_cirugia = models.AutoField(primary_key=True, db_column='ID_Cirugia')
    fecha = models.DateField(db_column='Fecha')
    tipo = models.CharField(max_length=50, db_column='Tipo')
    descripcion = models.CharField(max_length=250, blank=True, null=True, db_column='Descripcion')
    id_mascota = models.ForeignKey('Mascota', on_delete=models.DO_NOTHING, db_column='ID_Mascota')
    id_veterinario = models.ForeignKey('Veterinario', on_delete=models.DO_NOTHING, db_column='ID_Veterinario')

    class Meta:
        managed = False
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
        managed = False
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
        managed = False
        db_table = 'Consulta'

class Dueno(models.Model):
    id_dueno = models.AutoField(primary_key=True, db_column='ID_Dueno')
    nombre = models.CharField(max_length=50, db_column='Nombre')
    apellidos = models.CharField(max_length=50, db_column='Apellidos')
    telefono = models.CharField(max_length=20, blank=True, null=True, db_column='Telefono')
    direccion = models.CharField(max_length=100, blank=True, null=True, db_column='Direccion')
    email = models.CharField(max_length=50, blank=True, null=True, db_column='Email')

    class Meta:
        managed = False
        db_table = 'Dueno'

class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True, db_column='ID_Especialidad')
    nombre = models.CharField(max_length=50, db_column='Nombre')
    descripcion = models.CharField(max_length=200, blank=True, null=True, db_column='Descripcion')

    class Meta:
        managed = False
        db_table = 'Especialidad'

class Facturacion(models.Model):
    id_factura = models.AutoField(primary_key=True, db_column='ID_Factura')
    fecha = models.DateField(db_column='Fecha')
    id_cita = models.ForeignKey(Cita, on_delete=models.DO_NOTHING, db_column='ID_Cita')
    id_dueno = models.ForeignKey(Dueno, on_delete=models.DO_NOTHING, db_column='ID_Dueno')
    total = models.DecimalField(max_digits=10, decimal_places=2, db_column='Total')
    pagado = models.BooleanField(default=False, db_column='Pagado')

    class Meta:
        managed = False
        db_table = 'Facturacion'

class Hospitalizacion(models.Model):
    id_hospitalizacion = models.AutoField(primary_key=True, db_column='ID_Hospitalizacion')
    fechaingreso = models.DateField(db_column='FechaIngreso')
    fechaalta = models.DateField(blank=True, null=True, db_column='FechaAlta')
    motivo = models.CharField(max_length=200, blank=True, null=True, db_column='Motivo')
    id_mascota = models.ForeignKey('Mascota', on_delete=models.DO_NOTHING, db_column='ID_Mascota')
    id_veterinario = models.ForeignKey('Veterinario', on_delete=models.DO_NOTHING, db_column='ID_Veterinario')

    class Meta:
        managed = False
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
        managed = False
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
        managed = False
        db_table = 'Tratamiento'

class Veterinario(models.Model):
    id_veterinario = models.AutoField(primary_key=True, db_column='ID_Veterinario')
    nombre = models.CharField(max_length=50, db_column='Nombre')
    apellidos = models.CharField(max_length=50, db_column='Apellidos')
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.DO_NOTHING, db_column='ID_Especialidad')
    telefono = models.CharField(max_length=20, blank=True, null=True, db_column='Telefono')
    email = models.CharField(max_length=50, blank=True, null=True, db_column='Email')

    class Meta:
        managed = False
        db_table = 'Veterinario'
