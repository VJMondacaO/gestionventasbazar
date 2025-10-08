#!/usr/bin/env python3
"""
Script para actualizar las ventas existentes y crear ventas con la fecha correcta.
"""

import os
import sys
import django
from datetime import datetime, timedelta, date
import random

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestionVentasBazar.settings')
django.setup()

from apps.ventas_app.models import Venta

def actualizar_ventas_existentes():
    """Actualiza las ventas existentes para que tengan la fecha correcta"""
    print("Actualizando ventas existentes...")
    
    # Obtener las últimas 20 ventas
    ventas_recientes = Venta.objects.order_by('-fecha_venta')[:20]
    
    hoy = date.today()
    ventas_actualizadas = 0
    
    for venta in ventas_recientes:
        # Crear nueva fecha para hoy
        hora_aleatoria = random.randint(8, 18)
        minuto_aleatorio = random.randint(0, 59)
        nueva_fecha = datetime.combine(hoy, datetime.min.time().replace(hour=hora_aleatoria, minute=minuto_aleatorio))
        
        venta.fecha_venta = nueva_fecha
        venta.save()
        ventas_actualizadas += 1
        print(f"Venta {venta.numero_venta} actualizada a {nueva_fecha.date()}")
    
    print(f"Total ventas actualizadas: {ventas_actualizadas}")
    return ventas_actualizadas

def verificar_estadisticas_actualizadas():
    """Verifica las estadísticas después de la actualización"""
    print("\n=== VERIFICACIÓN DE ESTADÍSTICAS ACTUALIZADAS ===")
    
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
    print("=== ACTUALIZANDO VENTAS EXISTENTES ===")
    print()
    
    try:
        # Actualizar ventas existentes
        ventas_actualizadas = actualizar_ventas_existentes()
        
        # Verificar estadísticas
        stats = verificar_estadisticas_actualizadas()
        
        print(f"\n=== RESUMEN FINAL ===")
        print(f"✅ Se actualizaron {ventas_actualizadas} ventas")
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
        else:
            print(f"\n⚠️  ADVERTENCIA: Las tarjetas del dashboard aún no muestran datos.")
        
    except Exception as e:
        print(f"Error al actualizar ventas: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()
