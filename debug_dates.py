#!/usr/bin/env python3
"""
Script para debuggear las fechas y verificar por qué no se están mostrando las ventas de hoy.
"""

import os
import sys
import django
from datetime import datetime, timedelta

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestionVentasBazar.settings')
django.setup()

from apps.ventas_app.models import Venta

def debug_fechas():
    """Debug de fechas"""
    print("=== DEBUG DE FECHAS ===")
    
    hoy = datetime.now().date()
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

def main():
    """Función principal"""
    debug_fechas()

if __name__ == "__main__":
    main()
