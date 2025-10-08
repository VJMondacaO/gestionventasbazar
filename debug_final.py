#!/usr/bin/env python3
"""
Script final para debuggear las fechas y crear ventas que funcionen.
"""

import os
import sys
import django
from datetime import datetime, timedelta, date
import random
from django.utils import timezone

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestionVentasBazar.settings')
django.setup()

from apps.ventas_app.models import Venta
from apps.auth_app.models import Usuario
from apps.djangoVer.models import Productos, Clientes
from apps.ventas_app.models import ItemVenta

def debug_fechas_final():
    """Debug final de fechas"""
    print("=== DEBUG FINAL DE FECHAS ===")
    
    hoy = date.today()
    print(f"Fecha de hoy: {hoy}")
    print(f"Tipo de fecha de hoy: {type(hoy)}")
    
    # Verificar ventas
    total_ventas = Venta.objects.count()
    print(f"Total de ventas en la base de datos: {total_ventas}")
    
    # Verificar las últimas 5 ventas
    ultimas_ventas = Venta.objects.order_by('-fecha_venta')[:5]
    print(f"\nÚltimas 5 ventas:")
    for venta in ultimas_ventas:
        print(f"  Venta {venta.numero_venta}: {venta.fecha_venta} (fecha: {venta.fecha_venta.date()})")
    
    # Verificar ventas de hoy
    ventas_hoy = Venta.objects.filter(fecha_venta__date=hoy)
    print(f"\nVentas de hoy (fecha_venta__date={hoy}): {ventas_hoy.count()}")
    
    # Verificar ventas de hoy con diferentes filtros
    ventas_hoy_2 = Venta.objects.filter(fecha_venta__date=datetime.now().date())
    print(f"Ventas de hoy (datetime.now().date()): {ventas_hoy_2.count()}")
    
    # Verificar ventas de hoy con rango
    inicio_dia = datetime.combine(hoy, datetime.min.time())
    fin_dia = datetime.combine(hoy, datetime.max.time())
    ventas_hoy_3 = Venta.objects.filter(fecha_venta__gte=inicio_dia, fecha_venta__lte=fin_dia)
    print(f"Ventas de hoy (rango): {ventas_hoy_3.count()}")
    
    # Verificar ventas de la semana
    semana_pasada = hoy - timedelta(days=7)
    ventas_semana = Venta.objects.filter(fecha_venta__date__gte=semana_pasada)
    print(f"Ventas de la semana (desde {semana_pasada}): {ventas_semana.count()}")
    
    # Verificar ventas del mes
    mes_pasado = hoy - timedelta(days=30)
    ventas_mes = Venta.objects.filter(fecha_venta__date__gte=mes_pasado)
    print(f"Ventas del mes (desde {mes_pasado}): {ventas_mes.count()}")
    
    # Verificar ventas por fecha específica
    print(f"\nVentas por fecha específica:")
    for i in range(7):
        fecha = hoy - timedelta(days=i)
        count = Venta.objects.filter(fecha_venta__date=fecha).count()
        print(f"  {fecha}: {count} ventas")

def crear_venta_simple_hoy():
    """Crea una venta simple para hoy"""
    print("\n=== CREANDO VENTA SIMPLE PARA HOY ===")
    
    # Obtener datos necesarios
    vendedor = Usuario.objects.filter(username__startswith='vendedor').first()
    cliente = Clientes.objects.first()
    producto = Productos.objects.first()
    
    if not vendedor or not cliente or not producto:
        print("Error: No se encontraron datos necesarios")
        return None
    
    # Crear venta para hoy
    hoy = date.today()
    hora_aleatoria = random.randint(8, 18)
    minuto_aleatorio = random.randint(0, 59)
    fecha_naive = datetime.combine(hoy, datetime.min.time().replace(hour=hora_aleatoria, minute=minuto_aleatorio))
    fecha_venta = timezone.make_aware(fecha_naive)
    
    venta = Venta.objects.create(
        vendedor=vendedor,
        cliente=cliente,
        tipo_documento='boleta',
        forma_pago='efectivo',
        estado='completada',
        fecha_venta=fecha_venta
    )
    
    # Generar número de venta único
    venta.numero_venta = f"V{fecha_venta.strftime('%Y%m%d')}{venta.id:04d}"
    venta.save()
    
    # Agregar item a la venta
    ItemVenta.objects.create(
        venta=venta,
        producto=producto,
        cantidad=1,
        precio_unitario=producto.precio
    )
    
    venta.calcular_totales()
    venta.save()
    
    print(f"Venta creada: {venta.numero_venta} - ${venta.total:,.0f} CLP - {venta.fecha_venta.date()}")
    return venta

def verificar_estadisticas_finales():
    """Verifica las estadísticas finales"""
    print("\n=== VERIFICACIÓN FINAL DE ESTADÍSTICAS ===")
    
    hoy = date.today()
    
    # Ventas de hoy
    ventas_hoy = Venta.objects.filter(fecha_venta__date=hoy).count()
    print(f"Ventas de hoy: {ventas_hoy}")
    
    # Ingresos de hoy
    from django.db.models import Sum
    ingresos_hoy = Venta.objects.filter(fecha_venta__date=hoy).aggregate(
        total=Sum('total')
    )['total'] or 0
    print(f"Ingresos de hoy: ${ingresos_hoy:,.0f} CLP")
    
    # Ventas de la semana
    semana_pasada = hoy - timedelta(days=7)
    ventas_semana = Venta.objects.filter(fecha_venta__date__gte=semana_pasada).count()
    print(f"Ventas de la semana: {ventas_semana}")
    
    # Ingresos de la semana
    ingresos_semana = Venta.objects.filter(fecha_venta__date__gte=semana_pasada).aggregate(
        total=Sum('total')
    )['total'] or 0
    print(f"Ingresos de la semana: ${ingresos_semana:,.0f} CLP")
    
    # Ventas del mes
    mes_pasado = hoy - timedelta(days=30)
    ventas_mes = Venta.objects.filter(fecha_venta__date__gte=mes_pasado).count()
    print(f"Ventas del mes: {ventas_mes}")
    
    # Ingresos del mes
    ingresos_mes = Venta.objects.filter(fecha_venta__date__gte=mes_pasado).aggregate(
        total=Sum('total')
    )['total'] or 0
    print(f"Ingresos del mes: ${ingresos_mes:,.0f} CLP")
    
    # Mostrar algunas ventas de hoy
    ventas_hoy_lista = Venta.objects.filter(fecha_venta__date=hoy).order_by('-fecha_venta')[:5]
    print(f"\nVentas de hoy (últimas 5):")
    for venta in ventas_hoy_lista:
        print(f"  {venta.numero_venta}: {venta.fecha_venta.date()} - ${venta.total:,.0f} CLP")
    
    return {
        'ventas_hoy': ventas_hoy,
        'ingresos_hoy': ingresos_hoy,
        'ventas_semana': ventas_semana,
        'ingresos_semana': ingresos_semana,
        'ventas_mes': ventas_mes,
        'ingresos_mes': ingresos_mes
    }

def main():
    """Función principal"""
    print("=== DEBUG FINAL DE FECHAS Y VENTAS ===")
    print()
    
    try:
        # Debug de fechas
        debug_fechas_final()
        
        # Crear venta simple para hoy
        venta = crear_venta_simple_hoy()
        
        # Verificar estadísticas
        stats = verificar_estadisticas_finales()
        
        print(f"\n=== RESUMEN FINAL ===")
        print(f"✅ Las tarjetas del dashboard ahora deberían mostrar:")
        print(f"   - Ventas Hoy: {stats['ventas_hoy']}")
        print(f"   - Ingresos Hoy: ${stats['ingresos_hoy']:,.0f} CLP")
        print(f"   - Ventas Semana: {stats['ventas_semana']}")
        print(f"   - Ingresos Semana: ${stats['ingresos_semana']:,.0f} CLP")
        print(f"   - Ventas Mes: {stats['ventas_mes']}")
        print(f"   - Ingresos Mes: ${stats['ingresos_mes']:,.0f} CLP")
        
        if stats['ventas_hoy'] > 0:
            print(f"\n🎉 ¡ÉXITO! Las tarjetas del dashboard ahora deberían mostrar datos reales.")
            print(f"   Puedes acceder al dashboard en: http://127.0.0.1:8006/auth/")
            print(f"   Usuario: vendedor1")
            print(f"   Contraseña: vendedor123")
        else:
            print(f"\n⚠️  ADVERTENCIA: Las tarjetas del dashboard aún no muestran datos.")
            print(f"   Esto puede ser un problema de zona horaria en Django.")
        
    except Exception as e:
        print(f"Error en debug final: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()
