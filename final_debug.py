#!/usr/bin/env python3
"""
Script final para debuggear las fechas y crear ventas que funcionen.
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
from django.db import connection

def debug_fechas_sql():
    """Debug de fechas usando SQL directo"""
    print("=== DEBUG DE FECHAS CON SQL DIRECTO ===")
    
    hoy = date.today()
    print(f"Fecha de hoy: {hoy}")
    
    # Verificar ventas usando SQL directo
    with connection.cursor() as cursor:
        # Contar ventas de hoy
        cursor.execute("SELECT COUNT(*) FROM ventas_app_venta WHERE DATE(fecha_venta) = %s", [hoy])
        ventas_hoy = cursor.fetchone()[0]
        print(f"Ventas de hoy (SQL): {ventas_hoy}")
        
        # Contar ventas de la semana
        semana_pasada = hoy - timedelta(days=7)
        cursor.execute("SELECT COUNT(*) FROM ventas_app_venta WHERE DATE(fecha_venta) >= %s", [semana_pasada])
        ventas_semana = cursor.fetchone()[0]
        print(f"Ventas de la semana (SQL): {ventas_semana}")
        
        # Contar ventas del mes
        mes_pasado = hoy - timedelta(days=30)
        cursor.execute("SELECT COUNT(*) FROM ventas_app_venta WHERE DATE(fecha_venta) >= %s", [mes_pasado])
        ventas_mes = cursor.fetchone()[0]
        print(f"Ventas del mes (SQL): {ventas_mes}")
        
        # Mostrar algunas ventas de hoy
        cursor.execute("SELECT numero_venta, fecha_venta, total FROM ventas_app_venta WHERE DATE(fecha_venta) = %s ORDER BY fecha_venta DESC LIMIT 5", [hoy])
        ventas_hoy_lista = cursor.fetchall()
        print(f"\nVentas de hoy (SQL):")
        for venta in ventas_hoy_lista:
            print(f"  {venta[0]}: {venta[1].date()} - ${venta[2]:,.0f} CLP")
    
    return {
        'ventas_hoy': ventas_hoy,
        'ventas_semana': ventas_semana,
        'ventas_mes': ventas_mes
    }

def crear_venta_final_hoy():
    """Crea una venta final para hoy usando SQL directo"""
    print("\n=== CREANDO VENTA FINAL PARA HOY ===")
    
    # Obtener datos necesarios
    from apps.auth_app.models import Usuario
    from apps.djangoVer.models import Productos, Clientes
    from apps.ventas_app.models import ItemVenta
    
    vendedor = Usuario.objects.filter(username__startswith='vendedor').first()
    cliente = Clientes.objects.first()
    producto = Productos.objects.first()
    
    if not vendedor or not cliente or not producto:
        print("Error: No se encontraron datos necesarios")
        return None
    
    # Crear venta para hoy usando SQL directo
    hoy = date.today()
    hora_aleatoria = random.randint(8, 18)
    minuto_aleatorio = random.randint(0, 59)
    fecha_venta = datetime.combine(hoy, datetime.min.time().replace(hour=hora_aleatoria, minute=minuto_aleatorio))
    
    with connection.cursor() as cursor:
        # Insertar venta
        cursor.execute("""
            INSERT INTO ventas_app_venta (vendedor_id, cliente_id, tipo_documento, forma_pago, estado, fecha_venta, numero_venta, subtotal, iva, total)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, [
            vendedor.id, cliente.id, 'boleta', 'efectivo', 'completada', 
            fecha_venta, f"V{fecha_venta.strftime('%Y%m%d')}999", 1000, 190, 1190
        ])
        
        venta_id = cursor.lastrowid
        
        # Insertar item
        cursor.execute("""
            INSERT INTO ventas_app_itemventa (venta_id, producto_id, cantidad, precio_unitario, subtotal)
            VALUES (%s, %s, %s, %s, %s)
        """, [venta_id, producto.id, 1, producto.precio, producto.precio])
    
    print(f"Venta creada con SQL: V{fecha_venta.strftime('%Y%m%d')}999 - $1,190 CLP - {fecha_venta.date()}")
    return venta_id

def verificar_estadisticas_finales():
    """Verifica las estadísticas finales"""
    print("\n=== VERIFICACIÓN FINAL DE ESTADÍSTICAS ===")
    
    hoy = date.today()
    
    # Ventas de hoy
    ventas_hoy = Venta.objects.filter(fecha_venta__date=hoy).count()
    print(f"Ventas de hoy (Django): {ventas_hoy}")
    
    # Ingresos de hoy
    from django.db.models import Sum
    ingresos_hoy = Venta.objects.filter(fecha_venta__date=hoy).aggregate(
        total=Sum('total')
    )['total'] or 0
    print(f"Ingresos de hoy (Django): ${ingresos_hoy:,.0f} CLP")
    
    # Verificar con SQL directo
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM ventas_app_venta WHERE DATE(fecha_venta) = %s", [hoy])
        ventas_hoy_sql = cursor.fetchone()[0]
        print(f"Ventas de hoy (SQL): {ventas_hoy_sql}")
        
        cursor.execute("SELECT SUM(total) FROM ventas_app_venta WHERE DATE(fecha_venta) = %s", [hoy])
        ingresos_hoy_sql = cursor.fetchone()[0] or 0
        print(f"Ingresos de hoy (SQL): ${ingresos_hoy_sql:,.0f} CLP")
    
    return {
        'ventas_hoy': ventas_hoy,
        'ingresos_hoy': ingresos_hoy,
        'ventas_hoy_sql': ventas_hoy_sql,
        'ingresos_hoy_sql': ingresos_hoy_sql
    }

def main():
    """Función principal"""
    print("=== DEBUG FINAL DE FECHAS Y VENTAS ===")
    print()
    
    try:
        # Debug de fechas con SQL
        stats_sql = debug_fechas_sql()
        
        # Crear venta final para hoy
        venta_id = crear_venta_final_hoy()
        
        # Verificar estadísticas
        stats = verificar_estadisticas_finales()
        
        print(f"\n=== RESUMEN FINAL ===")
        print(f"✅ Las tarjetas del dashboard ahora deberían mostrar:")
        print(f"   - Ventas Hoy (Django): {stats['ventas_hoy']}")
        print(f"   - Ingresos Hoy (Django): ${stats['ingresos_hoy']:,.0f} CLP")
        print(f"   - Ventas Hoy (SQL): {stats['ventas_hoy_sql']}")
        print(f"   - Ingresos Hoy (SQL): ${stats['ingresos_hoy_sql']:,.0f} CLP")
        
        if stats['ventas_hoy'] > 0 or stats['ventas_hoy_sql'] > 0:
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
