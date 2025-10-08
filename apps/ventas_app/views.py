from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.utils import timezone
from datetime import datetime, date
import json

from .models import Venta, ItemVenta, ResumenDiario, ControlDia
from .forms import VentaForm, ItemVentaForm, BuscarVentaForm, ResumenDiarioForm
from apps.djangoVer.models import Productos, Clientes


@login_required
def nueva_venta(request):
    """
    Vista para crear una nueva venta con validaciones específicas
    """
    # Verificar si el día está cerrado
    hoy = date.today()
    control_dia = ControlDia.obtener_estado_dia(hoy)
    
    if control_dia.estado == 'cerrado':
        messages.error(request, 'No se pueden registrar ventas. El día está cerrado.')
        return redirect('ventas_app:dashboard_ventas')
    
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.vendedor = request.user
            
            # Generar número de venta único
            venta.numero_venta = Venta().generar_numero_venta()
            
            # Validaciones específicas para facturas
            if venta.tipo_documento == 'factura':
                if not venta.rut_cliente:
                    messages.error(request, 'El RUT es obligatorio para facturas')
                    return render(request, 'ventas_app/nueva_venta.html', {'form': form})
                if not venta.direccion_cliente:
                    messages.error(request, 'La dirección es obligatoria para facturas')
                    return render(request, 'ventas_app/nueva_venta.html', {'form': form})
                if not venta.comuna_cliente:
                    messages.error(request, 'La comuna es obligatoria para facturas')
                    return render(request, 'ventas_app/nueva_venta.html', {'form': form})
            
            venta.save()
            messages.success(request, f'Venta {venta.numero_venta} creada exitosamente')
            return redirect('ventas_app:agregar_items', venta_id=venta.id)
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario')
    else:
        form = VentaForm()
    
    return render(request, 'ventas_app/nueva_venta.html', {
        'form': form,
        'control_dia': control_dia
    })


@login_required
def agregar_items(request, venta_id):
    """
    Vista para agregar items a una venta
    """
    venta = get_object_or_404(Venta, id=venta_id)
    
    if request.method == 'POST':
        form = ItemVentaForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.venta = venta
            item.save()
            
            # Actualizar stock del producto
            producto = item.producto
            producto.stock -= item.cantidad
            producto.save()
            
            # Recalcular totales de la venta
            venta.calcular_totales()
            
            messages.success(request, f'Producto {item.producto.nombre} agregado a la venta')
            return redirect('ventas_app:agregar_items', venta_id=venta.id)
    else:
        form = ItemVentaForm()
    
    items = venta.items.all()
    return render(request, 'ventas_app/agregar_items.html', {
        'venta': venta,
        'form': form,
        'items': items
    })


@login_required
def eliminar_item(request, item_id):
    """
    Vista para eliminar un item de la venta
    """
    item = get_object_or_404(ItemVenta, id=item_id)
    venta = item.venta
    
    # Restaurar stock del producto
    producto = item.producto
    producto.stock += item.cantidad
    producto.save()
    
    item.delete()
    venta.calcular_totales()
    
    messages.success(request, 'Item eliminado de la venta')
    return redirect('ventas_app:agregar_items', venta_id=venta.id)


@login_required
def finalizar_venta(request, venta_id):
    """
    Vista para finalizar una venta
    """
    venta = get_object_or_404(Venta, id=venta_id)
    
    if venta.items.count() == 0:
        messages.error(request, 'No se puede finalizar una venta sin items')
        return redirect('ventas_app:agregar_items', venta_id=venta.id)
    
    venta.estado = 'completada'
    venta.save()
    
    # Generar resumen del día
    ResumenDiario.generar_resumen_dia(venta.fecha_venta.date())
    
    messages.success(request, f'Venta {venta.numero_venta} finalizada exitosamente')
    return redirect('ventas_app:detalle_venta', venta_id=venta.id)


@login_required
def detalle_venta(request, venta_id):
    """
    Vista para mostrar el detalle de una venta
    """
    venta = get_object_or_404(Venta, id=venta_id)
    items = venta.items.all()
    
    return render(request, 'ventas_app/detalle_venta.html', {
        'venta': venta,
        'items': items
    })


@login_required
def vista_previa_comprobante(request, venta_id):
    """
    Vista previa del comprobante antes de finalizar la venta
    """
    venta = get_object_or_404(Venta, id=venta_id)
    items = venta.items.all()
    
    if venta.items.count() == 0:
        messages.error(request, 'No se puede generar vista previa sin items')
        return redirect('ventas_app:agregar_items', venta_id=venta.id)
    
    return render(request, 'ventas_app/vista_previa_comprobante.html', {
        'venta': venta,
        'items': items
    })


@login_required
def generar_boleta(request, venta_id):
    """
    Vista para generar boleta/factura de una venta
    """
    venta = get_object_or_404(Venta, id=venta_id)
    items = venta.items.all()
    
    return render(request, 'ventas_app/boleta_venta.html', {
        'venta': venta,
        'items': items
    })


@login_required
def listar_ventas(request):
    """
    Vista para listar todas las ventas
    """
    form = BuscarVentaForm(request.GET)
    ventas = Venta.objects.all().order_by('-fecha_venta')
    
    if form.is_valid():
        tipo = form.cleaned_data.get('tipo_busqueda')
        termino = form.cleaned_data.get('termino')
        fecha_desde = form.cleaned_data.get('fecha_desde')
        fecha_hasta = form.cleaned_data.get('fecha_hasta')
        
        if tipo == 'numero' and termino:
            ventas = ventas.filter(numero_venta__icontains=termino)
        elif tipo == 'cliente' and termino:
            ventas = ventas.filter(cliente__nombre__icontains=termino)
        elif tipo == 'vendedor' and termino:
            ventas = ventas.filter(vendedor__username__icontains=termino)
        
        if fecha_desde:
            ventas = ventas.filter(fecha_venta__date__gte=fecha_desde)
        if fecha_hasta:
            ventas = ventas.filter(fecha_venta__date__lte=fecha_hasta)
    
    return render(request, 'ventas_app/listar_ventas.html', {
        'ventas': ventas,
        'form': form
    })


@login_required
def reportes_diarios(request):
    """
    Vista para mostrar reportes diarios detallados
    """
    if not request.user.es_jefe_ventas():
        messages.error(request, 'No tienes permisos para acceder a los reportes')
        return redirect('ventas_app:dashboard_ventas')
    
    # Obtener fecha del request o usar hoy
    fecha_str = request.GET.get('fecha')
    if fecha_str:
        try:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        except ValueError:
            fecha = date.today()
    else:
        fecha = date.today()
    
    # Obtener ventas del día
    ventas_dia = Venta.objects.filter(
        fecha_venta__date=fecha,
        estado='completada'
    ).order_by('-fecha_venta')
    
    # Estadísticas generales
    total_ventas = ventas_dia.count()
    total_boletas = ventas_dia.filter(tipo_documento='boleta').count()
    total_facturas = ventas_dia.filter(tipo_documento='factura').count()
    
    # Totales monetarios
    totales = ventas_dia.aggregate(
        total_neto=Sum('subtotal'),
        total_iva=Sum('iva'),
        total_bruto=Sum('total')
    )
    
    # Ventas por vendedor
    ventas_por_vendedor = ventas_dia.values('vendedor__username', 'vendedor__first_name', 'vendedor__last_name').annotate(
        cantidad_ventas=Count('id'),
        total_vendido=Sum('total')
    ).order_by('-total_vendido')
    
    # Ventas por tipo de documento
    ventas_por_tipo = ventas_dia.values('tipo_documento').annotate(
        cantidad=Count('id'),
        total=Sum('total')
    ).order_by('tipo_documento')
    
    # Productos más vendidos del día
    from .models import ItemVenta
    productos_vendidos = ItemVenta.objects.filter(
        venta__fecha_venta__date=fecha,
        venta__estado='completada'
    ).values('producto__nombre', 'producto__codigo').annotate(
        cantidad_vendida=Sum('cantidad'),
        total_vendido=Sum('subtotal')
    ).order_by('-cantidad_vendida')[:10]
    
    return render(request, 'ventas_app/reportes_diarios.html', {
        'fecha': fecha,
        'ventas_dia': ventas_dia,
        'total_ventas': total_ventas,
        'total_boletas': total_boletas,
        'total_facturas': total_facturas,
        'total_neto': totales['total_neto'] or 0,
        'total_iva': totales['total_iva'] or 0,
        'total_bruto': totales['total_bruto'] or 0,
        'ventas_por_vendedor': ventas_por_vendedor,
        'ventas_por_tipo': ventas_por_tipo,
        'productos_vendidos': productos_vendidos,
    })


@login_required
def resumen_diario(request):
    """
    Vista para generar y mostrar resúmenes diarios
    """
    if request.method == 'POST':
        form = ResumenDiarioForm(request.POST)
        if form.is_valid():
            fecha = form.cleaned_data['fecha']
            resumen = ResumenDiario.generar_resumen_dia(fecha)
            messages.success(request, f'Resumen del {fecha.strftime("%d/%m/%Y")} generado exitosamente')
            return redirect('ventas_app:detalle_resumen', resumen_id=resumen.id)
    else:
        form = ResumenDiarioForm()
    
    # Mostrar resúmenes recientes
    resumenes = ResumenDiario.objects.all().order_by('-fecha')[:10]
    
    return render(request, 'ventas_app/resumen_diario.html', {
        'form': form,
        'resumenes': resumenes
    })


@login_required
def detalle_resumen(request, resumen_id):
    """
    Vista para mostrar el detalle de un resumen diario
    """
    resumen = get_object_or_404(ResumenDiario, id=resumen_id)
    ventas_dia = Venta.objects.filter(
        fecha_venta__date=resumen.fecha,
        estado='completada'
    ).order_by('-fecha_venta')
    
    return render(request, 'ventas_app/detalle_resumen.html', {
        'resumen': resumen,
        'ventas_dia': ventas_dia
    })


@login_required
def dashboard_ventas(request):
    """
    Dashboard principal de ventas
    """
    hoy = date.today()
    
    # Estadísticas del día
    ventas_hoy = Venta.objects.filter(fecha_venta__date=hoy, estado='completada')
    total_ventas_hoy = ventas_hoy.count()
    total_dinero_hoy = ventas_hoy.aggregate(Sum('total'))['total__sum'] or 0
    
    # Estadísticas del mes
    mes_actual = hoy.replace(day=1)
    ventas_mes = Venta.objects.filter(
        fecha_venta__date__gte=mes_actual,
        estado='completada'
    )
    total_ventas_mes = ventas_mes.count()
    total_dinero_mes = ventas_mes.aggregate(Sum('total'))['total__sum'] or 0
    
    # Ventas recientes
    ventas_recientes = Venta.objects.filter(estado='completada').order_by('-fecha_venta')[:5]
    
    # Productos más vendidos
    productos_vendidos = ItemVenta.objects.values('producto__nombre').annotate(
        total_vendido=Sum('cantidad')
    ).order_by('-total_vendido')[:5]
    
    return render(request, 'ventas_app/dashboard_ventas.html', {
        'total_ventas_hoy': total_ventas_hoy,
        'total_dinero_hoy': total_dinero_hoy,
        'total_ventas_mes': total_ventas_mes,
        'total_dinero_mes': total_dinero_mes,
        'ventas_recientes': ventas_recientes,
        'productos_vendidos': productos_vendidos,
    })


# APIs para AJAX
@login_required
def obtener_precio_producto(request, producto_id):
    """
    API para obtener el precio de un producto
    """
    try:
        producto = Productos.objects.get(id=producto_id)
        return JsonResponse({
            'precio': float(producto.precio),
            'stock': producto.stock
        })
    except Productos.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)


@login_required
def obtener_clientes(request):
    """
    API para obtener lista de clientes
    """
    clientes = Clientes.objects.all().values('id', 'nombre', 'email')
    return JsonResponse(list(clientes), safe=False)


@login_required
def obtener_estadisticas_dashboard_ventas(request):
    """
    API endpoint para obtener estadísticas en tiempo real del dashboard de ventas
    """
    try:
        hoy = date.today()
        
        # Estadísticas del día
        ventas_hoy = Venta.objects.filter(fecha_venta__date=hoy, estado='completada')
        total_ventas_hoy = ventas_hoy.count()
        total_dinero_hoy = ventas_hoy.aggregate(Sum('total'))['total__sum'] or 0
        
        # Estadísticas del mes
        mes_actual = hoy.replace(day=1)
        ventas_mes = Venta.objects.filter(
            fecha_venta__date__gte=mes_actual,
            estado='completada'
        )
        total_ventas_mes = ventas_mes.count()
        total_dinero_mes = ventas_mes.aggregate(Sum('total'))['total__sum'] or 0
        
        # Ventas recientes (últimas 5)
        ventas_recientes = Venta.objects.filter(estado='completada').select_related('vendedor', 'cliente').order_by('-fecha_venta')[:5]
        
        # Productos más vendidos
        productos_vendidos = ItemVenta.objects.values('producto__nombre').annotate(
            total_vendido=Sum('cantidad')
        ).order_by('-total_vendido')[:5]
        
        estadisticas = {
            'total_ventas_hoy': total_ventas_hoy,
            'total_dinero_hoy': float(total_dinero_hoy),
            'total_ventas_mes': total_ventas_mes,
            'total_dinero_mes': float(total_dinero_mes),
            'ventas_recientes': [
                {
                    'id': venta.id,
                    'numero_venta': venta.numero_venta,
                    'cliente_nombre': venta.cliente.nombre if venta.cliente else "Cliente General",
                    'vendedor_nombre': venta.vendedor.get_full_name() if venta.vendedor.get_full_name() else venta.vendedor.username,
                    'total': float(venta.total),
                    'fecha_venta': venta.fecha_venta.strftime('%d/%m/%Y %H:%M')
                }
                for venta in ventas_recientes
            ],
            'productos_vendidos': [
                {
                    'nombre': producto['producto__nombre'],
                    'total_vendido': producto['total_vendido']
                }
                for producto in productos_vendidos
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
                'total_ventas_hoy': 0,
                'total_dinero_hoy': 0,
                'total_ventas_mes': 0,
                'total_dinero_mes': 0,
                'ventas_recientes': [],
                'productos_vendidos': [],
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        })


# Vistas para Control de Día (Solo Jefe de Ventas)
@login_required
def control_dia(request):
    """
    Vista para controlar el estado del día de ventas
    """
    if not request.user.es_jefe_ventas():
        messages.error(request, 'No tienes permisos para acceder a esta función')
        return redirect('ventas_app:dashboard_ventas')
    
    hoy = date.today()
    control_dia = ControlDia.obtener_estado_dia(hoy)
    
    # Obtener historial de controles
    controles_recientes = ControlDia.objects.all().order_by('-fecha')[:10]
    
    return render(request, 'ventas_app/control_dia.html', {
        'control_dia': control_dia,
        'controles_recientes': controles_recientes
    })


@login_required
def cerrar_dia(request):
    """
    Vista para cerrar el día de ventas
    """
    if not request.user.es_jefe_ventas():
        messages.error(request, 'No tienes permisos para cerrar el día')
        return redirect('ventas_app:dashboard_ventas')
    
    if request.method == 'POST':
        observaciones = request.POST.get('observaciones', '')
        hoy = date.today()
        control_dia = ControlDia.obtener_estado_dia(hoy)
        
        if control_dia.estado == 'cerrado':
            messages.warning(request, 'El día ya está cerrado')
        else:
            control_dia.cerrar_dia(request.user, observaciones)
            messages.success(request, f'Día {hoy.strftime("%d/%m/%Y")} cerrado exitosamente')
        
        return redirect('ventas_app:control_dia')
    
    return redirect('ventas_app:control_dia')


@login_required
def abrir_dia(request):
    """
    Vista para abrir el día de ventas
    """
    if not request.user.es_jefe_ventas():
        messages.error(request, 'No tienes permisos para abrir el día')
        return redirect('ventas_app:dashboard_ventas')
    
    hoy = date.today()
    control_dia = ControlDia.obtener_estado_dia(hoy)
    
    if control_dia.estado == 'abierto':
        messages.warning(request, 'El día ya está abierto')
    else:
        control_dia.abrir_dia(request.user)
        messages.success(request, f'Día {hoy.strftime("%d/%m/%Y")} abierto exitosamente')
    
    return redirect('ventas_app:control_dia')
