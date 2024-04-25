from django.shortcuts import render, redirect
# Create your views here.
from django.db.models import Q
from .models import Comunidad
from .models import Registro_Intervencion
from .forms import IntervencionForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'base/home.html')

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'El usuario no existe')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'El usuario o la contraseña no existen')

    context = {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect ('home')

def perfil(request):
    return render(request, 'base/perfil.html')

def comunidades(request):
    comunidades = Comunidad.objects.all()
    context = {'comunidades': comunidades}
    return render(request, 'base/comunidades.html', context)

def ingresar_beneficiaria(request):
    return render(request, 'base/ingresar_beneficiaria.html')

def ingresar_intervencion(request):
    return render(request, 'base/ingresar_intervencion.html')

def intervencion_form(request):
    form = IntervencionForm()
    if request.method == 'POST':
        form = IntervencionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'intervencion_form.html', context)

def actualizar_intervencion(request, pk):
    reg_intervencion = Registro_Intervencion.objects.get(id=pk)
    form = IntervencionForm(instance=reg_intervencion)
    
    if request.method == 'POST':
        form = IntervencionForm(request.POST, instance= reg_intervencion)
        if form.is_valid():
            form.save()
            return redirect('base/home')
    context = {'form': form}
    return render(request, 'intervencion_form.html', context)

def registro_intervencion(request, pk):
    registros = Registro_Intervencion.objects.get(pk=id)
    context = {'registros': registros}
    return render(request, 'base/registro_intervencion.html', context)

def ingresar_derivacion(request):
    return render(request, 'base/ingresar_derivacion.html')

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
