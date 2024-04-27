from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('perfil', views.perfil, name = "perfil"),
    path('comunidades', views.comunidades, name = "comunidades"),
    path('ingresar_beneficiaria', views.ingresar_beneficiaria, name = "ingresar_beneficiaria"),
    path('tus_registros', views.tus_registros, name = "tus_registros"),
    path('registro_intervencion', views.registro_intervencion, name = "registro_intervencion"),
    path('ingresar_intervencion', views.ingresar_intervencion, name = "ingresar_intervencion"),
    path('actualizar_intervencion/<str:pk>', views.actualizar_intervencion, name = "actualizar_intervencion"),
    path('ingresar_derivacion', views.ingresar_derivacion, name = "ingresar_derivacion"),
    path('eliminar_intervencion/<str:pk>', views.eliminarIntervencion, name = 'eliminar_intervencion')


]