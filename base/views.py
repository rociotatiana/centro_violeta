from django.shortcuts import render
# Create your views here.
from .models import Comunidad
from .models import Registro_Intervencion

def home(request):
    return render(request, 'base/home.html')

def perfil(request):
    return render(request, 'perfil.html')

def comunidades(request):
    comunidades = Comunidad.objects.all()
    context = {'comunidades': comunidades}
    return render(request, 'base/comunidades.html', context)

def ingresar_beneficiaria(request):
    return render(request, 'ingresar_beneficiaria.html')

def ingresar_intervencion(request):
    return render(request, 'ingresar_intervencion.html')

def registro_intervencion(request, pk):
    registros = Registro_Intervencion.objects.get(pk=id)
    context = {'registros': registros}
    return render(request, 'registro_intervencion.html', context)

def ingresar_derivacion(request):
    return render(request, 'ingresar_derivacion.html')
# COMUNIDADES:
# X Crear comunidades 

## BENEFICIARIAS:
# X Crear nueva beneficiaria


## PROGRAMA
# Incorporar nuevo programa

# REGISTRO DE INTERVENCION
# Crear RI
# Actualizar RI

# PLANILLA DE DERIVACIÓN
# Crear planilla

# INDICADORES
