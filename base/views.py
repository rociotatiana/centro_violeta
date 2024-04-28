from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.db.models import Q
from .models import User, Comunidad, Registro_Intervencion, Beneficiaria, Planilla_Derivacion
from .forms import IntervencionForm, BeneficiariaForm, DerivacionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'base/home.html')

## Inicio de sesión

def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=user.email)
        except:
            messages.error(request, print('El usuario no existe'))
        
        user = authenticate(request, email=email, password=password)

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


@login_required(login_url='login')
def perfil(request):
    return render(request, 'base/perfil.html')


## Vista de Beneficiarias 

@login_required(login_url='login')
def tus_beneficiarias(request):
    beneficiarias = Beneficiaria.objects.filter(profesional_que_ingresa = request.user.id)
    context = {'beneficiarias': beneficiarias}
    return render(request, 'base/tus_beneficiarias.html', context)

@login_required(login_url='login')
def ingresar_beneficiaria(request):
    form = BeneficiariaForm()
    if request.method == 'POST':
        form = BeneficiariaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, 'Has ingresado un valor no permitido')

    context = {'form': form}
    return render(request, 'base/beneficiaria_form.html', context)

@login_required(login_url='login')
def actualizar_beneficiaria(request, pk):
    beneficiaria = Beneficiaria.objects.get(id=pk)
    form = BeneficiariaForm(instance=beneficiaria)

    if request.user != beneficiaria.profesional_que_ingresa:
        return HttpResponse("No tienes permitida esta acción")
    
    if request.method == 'POST':
        form = BeneficiariaForm(request.POST, instance= beneficiaria)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/beneficiaria_form.html', context)

@login_required(login_url='login')
def eliminarBeneficiaria(request, pk):
    beneficiaria = Beneficiaria.objects.get(id=pk)
    if request.method == 'POST':
        beneficiaria.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': beneficiaria})


## Vista de Registros Intervención

@login_required(login_url='login')
def tus_registros(request):
    registros = Registro_Intervencion.objects.filter(profesional=request.user.id)
    beneficiarias = Beneficiaria.objects.filter(profesional_que_ingresa = request.user.id)
    context = {'registros': registros, 'beneficiarias': beneficiarias}
    return render(request, 'base/tus_registros.html', context)


@login_required(login_url='login')
def ingresar_intervencion(request):
    form = IntervencionForm()
    if request.method == 'POST':
        form = IntervencionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/intervencion_form.html', context)


@login_required(login_url='login')
def actualizar_intervencion(request, pk):
    reg_intervencion = Registro_Intervencion.objects.get(id=pk)
    form = IntervencionForm(instance=reg_intervencion)

    if request.user != reg_intervencion.profesional:
        return HttpResponse("No tienes permitida esta acción")
    
    if request.method == 'POST':
        form = IntervencionForm(request.POST, instance= reg_intervencion)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/intervencion_form.html', context)

@login_required(login_url='login')
def eliminarIntervencion(request, pk):
    reg_intervencion = Registro_Intervencion.objects.get(id=pk)
    if request.method == 'POST':
        reg_intervencion.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': reg_intervencion})


## Vista de Derivaciones 


@login_required(login_url='login')
def tus_derivaciones(request):
    derivaciones = Planilla_Derivacion.objects.filter(profesional_derivante=request.user.id)
    context = {'derivaciones': derivaciones}
    return render(request, 'base/tus_derivaciones.html', context)


@login_required(login_url='login')
def ingresar_derivacion(request):
    form = DerivacionForm()
    if request.method == 'POST':
        form = DerivacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/derivacion_form.html', context)


@login_required(login_url='login')
def actualizar_derivacion(request, pk):
    planilla_derivacion = Planilla_Derivacion.objects.get(id=pk)
    form = DerivacionForm(instance=planilla_derivacion)

    if request.user != planilla_derivacion.profesional_derivante:
        return HttpResponse("No tienes permitida esta acción")
    
    if request.method == 'POST':
        form = IntervencionForm(request.POST, instance= planilla_derivacion)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/derivacion_form.html', context)

@login_required(login_url='login')
def eliminarDerivacion(request, pk):
    planilla_derivacion = Planilla_Derivacion.objects.get(id=pk)
    if request.method == 'POST':
        planilla_derivacion.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': planilla_derivacion})


## Vista de Comunidades

@login_required(login_url='login')
def comunidades(request):
    comunidades = Comunidad.objects.all()
    context = {'comunidades': comunidades}
    return render(request, 'base/comunidades.html', context)