from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.db.models import Q
from .models import User, Comunidad, Registro_Intervencion
from .forms import IntervencionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required(login_url='login')
def perfil(request):
    return render(request, 'base/perfil.html')


@login_required(login_url='login')
def ingresar_beneficiaria(request):
    return render(request, 'base/ingresar_beneficiaria.html')


@login_required(login_url='login')
def tus_registros(request):
    registros = Registro_Intervencion.objects.all()
    context = {'registros': registros}
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

    if request.user != reg_intervencion.user:
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


@login_required(login_url='login')
def ingresar_derivacion(request):
    return render(request, 'base/ingresar_derivacion.html')



@login_required(login_url='login')
def registro_intervencion(request, pk):
    registros = Registro_Intervencion.objects.get(pk=id)
    context = {'registros': registros}
    return render(request, 'base/registro_intervencion.html', context)



@login_required(login_url='login')
def comunidades(request):
    comunidades = Comunidad.objects.all()
    context = {'comunidades': comunidades}
    return render(request, 'base/comunidades.html', context)