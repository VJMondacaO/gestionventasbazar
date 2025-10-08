"""
URL configuration for gestionVentasBazar project.

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
from django.shortcuts import redirect
from apps.djangoVer.views import (home, productosData, crearProducto, editarProducto, eliminarProducto,
                                         clientesData, crearCliente, editarCliente, eliminarCliente)

def redirect_to_index(request):
    """Redirige a la página de inicio"""
    return redirect('auth_app:index')

urlpatterns = [
    path('', redirect_to_index, name="home"),
    path('admin/', admin.site.urls),
    path('auth/', include('apps.auth_app.urls')),
    path('ventas/', include('apps.ventas_app.urls')),
    path('productos/', productosData, name="productosData"),
    path('crearProducto/', crearProducto, name="crearProducto"),
    path('editarProducto/<int:id>', editarProducto, name="editarProducto"),
    path('eliminarProducto/<int:id>', eliminarProducto, name="eliminarProducto"),
    path('clientes/', clientesData, name="clientesData"),
    path('crearCliente/', crearCliente, name="crearCliente"),
    path('editarCliente/<int:id>', editarCliente, name="editarCliente"),
    path('eliminarCliente/<int:id>', eliminarCliente, name="eliminarCliente"),
]
