from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Region(models.Model):
    nombre = models.CharField(max_length = 50)
    abreviatura = models.CharField(max_length = 5, null=True)

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    nombre = models.CharField(max_length = 30)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre
    
class Comuna(models.Model):
    nombre = models.CharField(max_length = 50)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre

class Institucion(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    tipo_origen = models.CharField(max_length=50, null=True)
    descripcion = models.TextField()
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Programa(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    descripcion = models.TextField()
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
    institucion_origen = models.ForeignKey(Institucion, on_delete=models.SET_NULL, null=True)
    #integrantes =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre

class Profesional(models.Model):
    rut = models.CharField(max_length=50, null=True)
    nombre = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    profesion = models.CharField(max_length=50, null=True)
    cargo_laboral = models.CharField(max_length=50, null=True)
    programa = models.ForeignKey(Programa, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Beneficiaria(models.Model):
    rut = models.CharField(max_length=50, null=True)
    nombre = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    fecha_nacimiento = models.DateField()
    situacion_laboral = models.CharField(max_length=50, null=True)
    numero_hijos = models.IntegerField()
    nivel_educativo = models.CharField(max_length=50, null=True)
    afp = models.CharField(max_length=50, null=True)
    seguro_medico = models.CharField(max_length=50, null=True)
    persona_confianza = models.CharField(max_length=50, null=True)
    casos_judicializados = models.CharField(max_length=50, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Planilla_Derivacion(models.Model):
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
    programa_destino = models.ForeignKey(Programa, on_delete=models.SET_NULL, null=True)
    beneficiaria = models.ForeignKey(Beneficiaria, on_delete=models.SET_NULL, null=True)
    profesional_derivante = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    descripcion = models.TextField()
    casos_judicializados = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.programa_destino
    
class Registro_Intervencion(models.Model):
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
    programa = models.ForeignKey(Programa, on_delete=models.SET_NULL, null=True)
    beneficiaria = models.ForeignKey(Beneficiaria, on_delete=models.SET_NULL, null=True)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    descripcion_intervencion = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.descripcion

class Comunidad(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.TextField()
    #integrantes
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Informe_indicadores(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Mensaje(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comunidades = models.ForeignKey(Comunidad, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]