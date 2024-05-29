from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.db.models import Q
from .models import User, Comunidad, Programa, Registro_Intervencion, Beneficiaria, Planilla_Derivacion, Mensaje, Tematica
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
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    comunidades = Comunidad.objects.filter(tematicas__nombre__contains=q)
    tematicas = Tematica.objects.all()
    mensajes_comunidades = Mensaje.objects.all()
    context = {'comunidades': comunidades, 'mensajes_comunidades': mensajes_comunidades, 'tematicas': tematicas}
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
from datetime import date

def chart_beneficiarias(request):
    # Obtiene todos los datos de las beneficiarias
    beneficiarias = Beneficiaria.objects.filter(profesional_que_ingresa__programa = request.user.programa)

    # Gráfico en barra de nivel educativo
    niveles_educativos = beneficiarias.values('nivel_educativo').annotate(count=Count('nivel_educativo')).order_by('nivel_educativo')
    fig_nivel_educativo = px.bar(
        x=[ne['nivel_educativo'] for ne in niveles_educativos],
        y=[ne['count'] for ne in niveles_educativos],
        labels={'x': 'Nivel Educativo', 'y': 'Cantidad'},
        title='Distribución del Nivel Educativo'
    )
    chart_nivel_educativo = fig_nivel_educativo.to_html()

    # Gráfico en barra de AFP
    afps = beneficiarias.values('afp').annotate(count=Count('afp')).order_by('afp')
    fig_afp = px.bar(
        x=[a['afp'] for a in afps],
        y=[a['count'] for a in afps],
        labels={'x': 'AFP', 'y': 'Cantidad'},
        title='Distribución de AFP'
    )
    chart_afp = fig_afp.to_html()

    # Gráfico en barra de número de hijos
    num_hijos = beneficiarias.values('numero_hijos').annotate(count=Count('numero_hijos')).order_by('numero_hijos')
    fig_num_hijos = px.bar(
        x=[nh['numero_hijos'] for nh in num_hijos],
        y=[nh['count'] for nh in num_hijos],
        labels={'x': 'Número de Hijos', 'y': 'Cantidad'},
        title='Distribución del Número de Hijos'
    )
    chart_num_hijos = fig_num_hijos.to_html()

    # Gráfico en barra de seguro médico
    seguros_medicos = beneficiarias.values('seguro_medico').annotate(count=Count('seguro_medico')).order_by('seguro_medico')
    fig_seguro_medico = px.bar(
        x=[sm['seguro_medico'] for sm in seguros_medicos],
        y=[sm['count'] for sm in seguros_medicos],
        labels={'x': 'Seguro Médico', 'y': 'Cantidad'},
        title='Distribución del Seguro Médico'
    )
    chart_seguro_medico = fig_seguro_medico.to_html()

    # Histograma de edad de beneficiarias
    # Calcula la edad basada en la fecha de nacimiento
    today = date.today()
    edades = [(today.year - b.fecha_nacimiento.year - ((today.month, today.day) < (b.fecha_nacimiento.month, b.fecha_nacimiento.day))) for b in beneficiarias]
    fig_edades = px.bar(
        x=edades,
        labels={'x': 'Edad', 'y': 'Cantidad'},
        title='Distribución de Edad de Beneficiarias'
    )
    chart_edades = fig_edades.to_html()

    # Pasar gráficos al contexto del template
    context = {
        'chart_nivel_educativo': chart_nivel_educativo,
        'chart_afp': chart_afp,
        'chart_num_hijos': chart_num_hijos,
        'chart_seguro_medico': chart_seguro_medico,
        'chart_edades': chart_edades
    }
    return render(request, "base/chart2.html", context)


def graficos(request):
    usuario = User.objects.get(id = request.user.id)
    # Gráfico de Registros
    registros = (
        Registro_Intervencion.objects.filter(programa=request.user.programa)
        .annotate(date=TruncDate('created'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )

    dates_registros = [r['date'] for r in registros]
    counts_registros = [r['count'] for r in registros]

    fig_registros = px.line(
        x=dates_registros,
        y=counts_registros,
        labels={'x': 'Fecha', 'y': 'Cantidad de Registros'},
        title='Registros por Día',
        range_y=[0, 10],
        markers=True
    )

    chart_registros = fig_registros.to_html()

    # Gráfico de Derivaciones Emitidas
    derivaciones = (
        Planilla_Derivacion.objects.filter(profesional_derivante__programa=request.user.programa)
        .annotate(date=TruncDate('created'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )

    dates_derivaciones = [d['date'] for d in derivaciones]
    counts_derivaciones = [d['count'] for d in derivaciones]

    fig_derivaciones = px.line(
        x=dates_derivaciones,
        y=counts_derivaciones,
        labels={'x': 'Fecha', 'y': 'Cantidad de Derivaciones'},
        title='Derivaciones Emitidas por Día',
        range_y=[0, 10],
        markers=True
    )

    chart_derivaciones = fig_derivaciones.to_html()

    # Grafico Derivaciones Recibidas

    re_derivaciones = (
        Planilla_Derivacion.objects.filter(programa_destino=request.user.programa)
        .annotate(date=TruncDate('created'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )

    dates_re_derivaciones = [d['date'] for d in re_derivaciones]
    counts_re_derivaciones = [d['count'] for d in re_derivaciones]

    fig_re_derivaciones = px.line(
        x=dates_re_derivaciones,
        y=counts_re_derivaciones,
        labels={'x': 'Fecha', 'y': 'Cantidad de Derivaciones'},
        title='Derivaciones Emitidas por Día',
        range_y=[0, 10],
        markers=True
    )

    chart_re_derivaciones = fig_re_derivaciones.to_html()

    # Pasar gráficos al contexto del template
    context = {'usuario':usuario, 'chart_registros': chart_registros, 'chart_derivaciones': chart_derivaciones, 
               'chart_re_derivaciones': chart_re_derivaciones}
    return render(request, "base/chart.html", context)