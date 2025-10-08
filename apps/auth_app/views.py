from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.db import models
from django.http import JsonResponse
from .forms import LoginForm
from apps.ventas_app.models import Venta
from apps.djangoVer.models import Productos, Clientes
from django.db.models import Sum, Count
from datetime import datetime, timedelta
import json


def index_view(request):
    """
    Vista para la página de inicio del sistema
    """
    # Si el usuario ya está autenticado, redirigir al dashboard
    if request.user.is_authenticated:
        return redirect('auth_app:dashboard')
    
    # Obtener estadísticas generales para mostrar en la página de inicio
    try:
        total_ventas = Venta.objects.count()
        total_productos = Productos.objects.count()
        total_clientes = Clientes.objects.count()
        
        # Ventas del día
        hoy = datetime.now().date()
        ventas_hoy = Venta.objects.filter(fecha_venta__date=hoy).count()
        
        # Productos con stock bajo (menos de 10 unidades)
        productos_stock_bajo = Productos.objects.filter(stock__lt=10).count()
        
        estadisticas = {
            'total_ventas': total_ventas,
            'total_productos': total_productos,
            'total_clientes': total_clientes,
            'ventas_hoy': ventas_hoy,
            'productos_stock_bajo': productos_stock_bajo,
        }
    except:
        estadisticas = {
            'total_ventas': 0,
            'total_productos': 0,
            'total_clientes': 0,
            'ventas_hoy': 0,
            'productos_stock_bajo': 0,
        }
    
    return render(request, 'auth_app/index.html', {'estadisticas': estadisticas})


def login_view(request):
    """
    Vista para el inicio de sesión
    """
    if request.user.is_authenticated:
        return redirect('auth_app:dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido, {user.get_full_name() or user.username}!')
                
                # Redirigir según el rol del usuario
                if user.es_jefe_ventas():
                    return redirect('auth_app:jefe_ventas_dashboard')
                elif user.es_vendedor():
                    return redirect('auth_app:vendedor_dashboard')
                else:
                    return redirect('auth_app:dashboard')
            else:
                messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = LoginForm()
    
    return render(request, 'auth_app/login.html', {'form': form})


def logout_view(request):
    """
    Vista para cerrar sesión
    """
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('auth_app:index')


@login_required
def dashboard(request):
    """
    Dashboard principal con estadísticas en tiempo real
    """
    user = request.user
    
    # Obtener estadísticas generales
    try:
        # Estadísticas de ventas
        total_ventas = Venta.objects.count()
        ventas_hoy = Venta.objects.filter(fecha_venta__date=datetime.now().date()).count()
        ventas_semana = Venta.objects.filter(fecha_venta__date__gte=datetime.now().date() - timedelta(days=7)).count()
        
        # Estadísticas de productos
        total_productos = Productos.objects.count()
        productos_stock_bajo = Productos.objects.filter(stock__lt=10).count()
        productos_sin_stock = Productos.objects.filter(stock=0).count()
        
        # Estadísticas de clientes
        total_clientes = Clientes.objects.count()
        clientes_nuevos_mes = Clientes.objects.filter(fecha_registro__gte=datetime.now().date() - timedelta(days=30)).count()
        
        # Ventas por estado
        ventas_pendientes = Venta.objects.filter(estado='pendiente').count()
        ventas_completadas = Venta.objects.filter(estado='completada').count()
        
        # Ventas recientes (últimas 5)
        ventas_recientes = Venta.objects.select_related('vendedor', 'cliente').order_by('-fecha_venta')[:5]
        
        # Productos más vendidos (últimos 30 días)
        from django.db.models import Sum
        productos_mas_vendidos = Productos.objects.annotate(
            total_vendido=Sum('itemventa__cantidad', 
                            filter=models.Q(itemventa__venta__fecha_venta__gte=datetime.now().date() - timedelta(days=30)))
        ).filter(total_vendido__gt=0).order_by('-total_vendido')[:5]
        
        estadisticas = {
            'total_ventas': total_ventas,
            'ventas_hoy': ventas_hoy,
            'ventas_semana': ventas_semana,
            'total_productos': total_productos,
            'productos_stock_bajo': productos_stock_bajo,
            'productos_sin_stock': productos_sin_stock,
            'total_clientes': total_clientes,
            'clientes_nuevos_mes': clientes_nuevos_mes,
            'ventas_pendientes': ventas_pendientes,
            'ventas_completadas': ventas_completadas,
            'ventas_recientes': ventas_recientes,
            'productos_mas_vendidos': productos_mas_vendidos,
        }
    except Exception as e:
        estadisticas = {
            'total_ventas': 0,
            'ventas_hoy': 0,
            'ventas_semana': 0,
            'total_productos': 0,
            'productos_stock_bajo': 0,
            'productos_sin_stock': 0,
            'total_clientes': 0,
            'clientes_nuevos_mes': 0,
            'ventas_pendientes': 0,
            'ventas_completadas': 0,
            'ventas_recientes': [],
            'productos_mas_vendidos': [],
        }
    
    context = {
        'user': user,
        'estadisticas': estadisticas,
    }
    
    if user.es_jefe_ventas():
        return render(request, 'auth_app/jefe_ventas_dashboard.html', context)
    elif user.es_vendedor():
        return render(request, 'auth_app/vendedor_dashboard.html', context)
    else:
        return render(request, 'auth_app/dashboard.html', context)


@login_required
def vendedor_dashboard(request):
    """
    Dashboard específico para vendedores - Redirige al sistema de ventas
    """
    if not request.user.es_vendedor():
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('auth_app:dashboard')
    
    return redirect('ventas_app:dashboard_ventas')


@login_required
def jefe_ventas_dashboard(request):
    """
    Dashboard específico para jefes de ventas - Redirige al sistema de ventas
    """
    if not request.user.es_jefe_ventas():
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('auth_app:dashboard')
    
    return redirect('ventas_app:dashboard_ventas')


@login_required
def obtener_estadisticas_tiempo_real(request):
    """
    API endpoint para obtener estadísticas en tiempo real del dashboard
    """
    try:
        # Estadísticas de ventas
        total_ventas = Venta.objects.count()
        ventas_hoy = Venta.objects.filter(fecha_venta__date=datetime.now().date()).count()
        ventas_semana = Venta.objects.filter(fecha_venta__date__gte=datetime.now().date() - timedelta(days=7)).count()
        
        # Estadísticas de productos
        total_productos = Productos.objects.count()
        productos_stock_bajo = Productos.objects.filter(stock__lt=10).count()
        productos_sin_stock = Productos.objects.filter(stock=0).count()
        
        # Estadísticas de clientes
        total_clientes = Clientes.objects.count()
        clientes_nuevos_mes = Clientes.objects.filter(fecha_registro__gte=datetime.now().date() - timedelta(days=30)).count()
        
        # Ventas por estado
        ventas_pendientes = Venta.objects.filter(estado='pendiente').count()
        ventas_completadas = Venta.objects.filter(estado='completada').count()
        
        # Ventas recientes (últimas 5)
        ventas_recientes = Venta.objects.select_related('vendedor', 'cliente').order_by('-fecha_venta')[:5]
        
        # Productos más vendidos (últimos 30 días)
        productos_mas_vendidos = Productos.objects.annotate(
            total_vendido=Sum('itemventa__cantidad', 
                            filter=models.Q(itemventa__venta__fecha_venta__gte=datetime.now().date() - timedelta(days=30)))
        ).filter(total_vendido__gt=0).order_by('-total_vendido')[:5]
        
        estadisticas = {
            'total_ventas': total_ventas,
            'ventas_hoy': ventas_hoy,
            'ventas_semana': ventas_semana,
            'total_productos': total_productos,
            'productos_stock_bajo': productos_stock_bajo,
            'productos_sin_stock': productos_sin_stock,
            'total_clientes': total_clientes,
            'clientes_nuevos_mes': clientes_nuevos_mes,
            'ventas_pendientes': ventas_pendientes,
            'ventas_completadas': ventas_completadas,
            'ventas_recientes': [
                {
                    'numero_venta': venta.numero_venta,
                    'cliente_nombre': venta.cliente.nombre if venta.cliente else "Cliente General",
                    'fecha_venta': venta.fecha_venta.strftime('%d/%m/%Y %H:%M'),
                    'total': float(venta.total),
                    'estado': venta.get_estado_display(),
                    'estado_class': 'success' if venta.estado == 'completada' else 'warning'
                }
                for venta in ventas_recientes
            ],
            'productos_mas_vendidos': [
                {
                    'nombre': producto.nombre,
                    'total_vendido': producto.total_vendido or 0
                }
                for producto in productos_mas_vendidos
            ],
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return JsonResponse({
            'success': True,
            'data': estadisticas
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e),
            'data': {
                'total_ventas': 0,
                'ventas_hoy': 0,
                'ventas_semana': 0,
                'total_productos': 0,
                'productos_stock_bajo': 0,
                'productos_sin_stock': 0,
                'total_clientes': 0,
                'clientes_nuevos_mes': 0,
                'ventas_pendientes': 0,
                'ventas_completadas': 0,
                'ventas_recientes': [],
                'productos_mas_vendidos': [],
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        })
