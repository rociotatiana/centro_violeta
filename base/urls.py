from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('perfil', views.perfil, name = "perfil"),
    path('comunidades', views.comunidades, name = "comunidades"),
    path('tus_beneficiarias', views.tus_beneficiarias, name = "tus_beneficiarias"),
    path('ingresar_beneficiaria', views.ingresar_beneficiaria, name = "ingresar_beneficiaria"),
    path('actualizar_beneficiaria/<str:pk>', views.actualizar_beneficiaria, name = "actualizar_beneficiaria"),
    path('eliminar_beneficiaria/<str:pk>', views.eliminarBeneficiaria, name = "eliminar_beneficiaria"),
    path('tus_registros', views.tus_registros, name = "tus_registros"),
    path('ingresar_intervencion', views.ingresar_intervencion, name = "ingresar_intervencion"),
    path('actualizar_intervencion/<str:pk>', views.actualizar_intervencion, name = "actualizar_intervencion"),
    path('eliminar_intervencion/<str:pk>', views.eliminarIntervencion, name = 'eliminar_intervencion'),
    path('tus_derivaciones', views.tus_derivaciones, name = "tus_derivaciones"),
    path('ingresar_derivacion', views.ingresar_derivacion, name = "ingresar_derivacion"),
    path('actualizar_derivacion/<str:pk>', views.actualizar_derivacion, name = "actualizar_derivacion"),
    path('eliminar_derivacion/<str:pk>', views.eliminarDerivacion, name = 'eliminar_derivacion'),



]