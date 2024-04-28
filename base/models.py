from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    cargo_profesional = models.CharField(max_length=200, null=True)
    programa = models.ForeignKey('Programa', on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
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

class Beneficiaria(models.Model):
    profesional_que_ingresa = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    rut = models.CharField(unique=True, max_length=50, null=True)
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
    contacto_persona_confianza = models.CharField(max_length=50, null=True)
    casos_judicializados = models.CharField(max_length=50, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rut
    
class Planilla_Derivacion(models.Model):
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
    programa_destino = models.ForeignKey(Programa, on_delete=models.SET_NULL, null=True)
    beneficiaria = models.ForeignKey(Beneficiaria, on_delete=models.SET_NULL, null=True)
    profesional_derivante = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    descripcion = models.TextField()
    casos_judicializados = models.TextField()
    #documento = models.FileField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return str(self.profesional_derivante)
    
class Registro_Intervencion(models.Model):
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
    programa = models.ForeignKey(Programa, on_delete=models.SET_NULL, null=True)
    beneficiaria = models.ForeignKey(Beneficiaria, on_delete=models.SET_NULL, null=True)
    profesional = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    descripcion = models.TextField()
    #documento = models.FileField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.descripcion

class Comunidad(models.Model):
    administrador = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
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