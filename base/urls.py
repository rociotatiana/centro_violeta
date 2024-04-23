from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('perfil', views.perfil, name = "perfil"),
    path('comunidades', views.comunidades, name = "comunidades"),
    path('ingresar_beneficiaria', views.ingresar_beneficiaria, name = "ingresar_beneficiaria"),
    path('registro_intervencion', views.registro_intervencion, name = "registro_intervencion"),
    path('ingresar_intervencion', views.ingresar_intervencion, name = "ingresar_intervencion"),
    path('ingresar_derivacion', views.ingresar_derivacion, name = "ingresar_derivacion"),


]