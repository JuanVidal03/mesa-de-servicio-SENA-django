"""
URL configuration for ProyectoMesaServicio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio),
    path('login/', views.login),
    path('inicioAdministrador/', views.inicioAdministrador),
    path('inicioTecnico/', views.inicioTecnico),
    path('inicioEmpleado/', views.inicioEmpleado),
    path('vistaSolicitud/', views.vistaSolicitud),
    path('registroSolicitud/', views.registroSolicitud),
    path('listarCasosParaAsignar/',views.listarCasos),
    path('asignarTecnicoCaso/', views.asignarTecnicoCaso),
    path('listarCasosAsignados/', views.listarCasosAsignadosTecnico),
    path('solucionarCaso/',views.solucionarCaso),
    path('listarSolicitudes/', views.listarSolicitudes),
    path('vistaGestionarUsuarios/', views.vistaGestionarUsuarios),
    path('vistaRegistrarUsuario/', views.vistaRegistrarUsuario),
    path('registrarUsuario/', views.registrarUsuario),
    path('recuperarClave/', views.recuperarClave),
    path('reportesEstadisticos/', views.estadisticas),
    path('pdfSolicitudes/', views.generarPdfSolicitudes),
    path('salir/', views.salir)
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
