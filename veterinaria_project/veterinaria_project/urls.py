"""
URL configuration for veterinaria_project project.

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
from django.contrib import admin
from django.urls import path, include
from veterinaria.views import lista_citas, lista_mascotas, crear_cita, crear_mascota, editar_cita, editar_mascota, eliminar_cita, eliminar_mascota, home, generar_reporte_citas, generar_reporte

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/', include('veterinaria.urls')),
    path('mascotas/', lista_mascotas, name='lista_mascotas'),
    path('mascotas/crear/', crear_mascota, name='crear_mascota'),
    path('mascotas/editar/<int:pk>/', editar_mascota, name='editar_mascota'),
    path('mascotas/eliminar/<int:pk>/', eliminar_mascota, name='eliminar_mascota'),
    path('citas/', lista_citas, name='lista_citas'),
    path('citas/crear/', crear_cita, name='crear_cita'),
    path('citas/editar/<int:pk>/', editar_cita, name='editar_cita'),
    path('citas/eliminar/<int:pk>/', eliminar_cita, name='eliminar_cita'),
    path('reportes/citas/', generar_reporte_citas, name='reporte_citas'),
    path('generar-reporte/', generar_reporte, name='generar_reporte'),
]
