from django.urls import path
from ProyectoWebApp import views

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/', include('app_inventario.urls')),
    path('finanzas/', include('app_finanzas.urls')),
    path('pedidos/', include('app_pedidos.urls')),
    path('pagos/', include('app_pagos.urls')),
    path('usuarios/', include('app_usuarios.urls')),
    path('reportes/', include('app_reportes.urls')),
]