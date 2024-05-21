from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.db.models import Q
from .models import User, Comunidad, Programa, Registro_Intervencion, Beneficiaria, Planilla_Derivacion, Mensaje
from .forms import IntervencionForm, BeneficiariaForm, DerivacionForm, ComunidadForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

## HOME 
def home(request):
    comunidades = Comunidad.objects.all()

    programas = Programa.objects.all()
    mensajes_comunidades = Mensaje.objects.all()

    context = {'comunidades': comunidades, 'programas': programas, 'mensajes_comunidades': mensajes_comunidades}
    return render(request, 'base/home.html', context)

def dashboard(request):
    return render (request, "base/dashboard.html")

## Inicio de sesión

def loginPage(request):
    page = "login"
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

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect ('home')

def registerUser(request):
    page = 'register'
    return render(request, 'base/login_register.html')

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
def derivaciones_recibidas(request):
    derivaciones = Planilla_Derivacion.objects.filter(programa_destino=request.user.programa)
    context = {'derivaciones': derivaciones}
    return render(request, 'base/derivaciones_recibidas.html', context)


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
def comunidad(request, pk):
    comunidad = Comunidad.objects.get(id=pk)
    comunidad_mensajes = comunidad.mensaje_set.all().order_by('-created')
    participantes = comunidad.participantes.all()
    if request.method == 'POST':
        mensaje = Mensaje.objects.create(
            usuario = request.user,
            comunidad = comunidad,
            body = request.POST.get('body')
        )
        comunidad.participantes.add(request.user)
        return redirect('comunidad', pk=comunidad.id)
    context = {'comunidad': comunidad, 'comunidad_mensajes': comunidad_mensajes, 
               'participantes': participantes}
    return render(request, 'base/comunidad.html', context)


@login_required(login_url='login')
def explora_comunidades(request):
    comunidades = Comunidad.objects.all()
    mensajes_comunidades = Mensaje.objects.all()
    context = {'comunidades': comunidades, 'mensajes_comunidades': mensajes_comunidades}
    return render(request, 'base/explora_comunidades.html', context)


@login_required(login_url='login')
def crear_comunidad(request):
    form = ComunidadForm()
    if request.method == 'POST':
        form = ComunidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/comunidad_form.html', context)


@login_required(login_url='login')
def actualizar_comunidad(request, pk):
    comunidad = Comunidad.objects.get(id=pk)
    form = ComunidadForm(instance=comunidad)

    if request.user != comunidad.administrador:
        return HttpResponse("No tienes permitida esta acción")
    
    if request.method == 'POST':
        form = ComunidadForm(request.POST, instance= comunidad)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/comunidad_form.html', context)

@login_required(login_url='login')
def eliminarComunidad(request, pk):
    comunidad = Comunidad.objects.get(id=pk)
    if request.method == 'POST':
        comunidad.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': comunidad})


## Eliminar Mensaje
@login_required(login_url='login')
def eliminarMensaje(request, pk):
    mensaje = Mensaje.objects.get(id=pk)
    if request.user != mensaje.usuario:
        return HttpResponse("No puedes realizar esta accion")
    if request.method == 'POST':
        mensaje.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': mensaje})


#### Gráficos #######

import plotly.express as px
from django.db.models.functions import TruncDate
from django.db.models import Count

import plotly.express as px
from django.db.models.functions import TruncDate
from django.db.models import Count
from django.shortcuts import render
from .models import Registro_Intervencion

def chart_registros(request):
    # Agrupar los registros por fecha y contar la cantidad de registros por cada fecha
    registros = (
        Registro_Intervencion.objects.filter(programa=request.user.programa)
        .annotate(date=TruncDate('created'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )

    # Extraer las fechas y los conteos
    dates = [r['date'] for r in registros]
    counts = [r['count'] for r in registros]

    # Determinar los límites del eje y 
    y_min = 0
    y_max = max(counts) + 10  

    # Crear el gráfico con Plotly, añadiendo marcadores para los puntos
    fig = px.line(
        x=dates,
        y=counts,
        labels={'x': 'Fecha', 'y': 'Cantidad de Registros'},
        title='Registros de Intervención por Día',
        range_y=[y_min, y_max],
        markers=True
    )

    # Convertir el gráfico a HTML
    chart = fig.to_html()

    # Pasar el gráfico al contexto del template
    context = {'chart': chart}
    return render(request, "base/chart.html", context)


def chart_derivaciones_emitidas(request):
    derivaciones = (
        Planilla_Derivacion.objects.filter(profesional_derivante__programa=request.user.programa)
        .annotate(date=TruncDate('created'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )

    # Extraer las fechas y los conteos
    dates = [r['date'] for r in derivaciones]
    counts = [r['count'] for r in derivaciones]

    # Determinar los límites del eje y 
    y_min = 0
    y_max = max(counts) + 10  

    # Crear el gráfico con Plotly, añadiendo marcadores para los puntos
    fig = px.line(
        x=dates,
        y=counts,
        labels={'x': 'Fecha', 'y': 'Cantidad de Derivaciones'},
        title='Derivaciones por Día',
        range_y=[y_min, y_max],
        markers=True
    )

    # Convertir el gráfico a HTML
    chart = fig.to_html()

    # Pasar el gráfico al contexto del template
    context = {'chart': chart}
    return render(request, "base/chart2.html", context)

def grafico_derivaciones_recibidas(request):
    pass
