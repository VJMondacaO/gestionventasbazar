#!/usr/bin/env python3
"""
Script para crear ventas con fecha local correcta.
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
from apps.auth_app.models import Usuario
from apps.djangoVer.models import Productos, Clientes
from apps.ventas_app.models import ItemVenta

def crear_ventas_locales_hoy():
    """Crea ventas para hoy usando fecha local"""
    print("Creando ventas locales para hoy...")
    
    # Obtener datos necesarios
    vendedores = Usuario.objects.filter(username__startswith='vendedor')[:3]
    clientes = Clientes.objects.all()
    productos = Productos.objects.all()
    
    # Crear ventas para hoy
    hoy = date.today()
    ventas_creadas = 0
    
    for i in range(15):  # Crear 15 ventas para hoy
        # Crear fecha local para hoy
        hora_aleatoria = random.randint(8, 18)
        minuto_aleatorio = random.randint(0, 59)
        fecha_venta = datetime.combine(hoy, datetime.min.time().replace(hour=hora_aleatoria, minute=minuto_aleatorio))
        
        vendedor = random.choice(vendedores)
        cliente = random.choice(clientes)
        tipo_documento = random.choice(['boleta', 'factura'])
        forma_pago = random.choice(['efectivo', 'transferencia', 'tarjeta_debito', 'tarjeta_credito'])
        
        venta = Venta.objects.create(
            vendedor=vendedor,
            cliente=cliente,
            tipo_documento=tipo_documento,
            forma_pago=forma_pago,
            estado='completada',
            fecha_venta=fecha_venta
        )
        
        # Generar número de venta único
        venta.numero_venta = f"V{fecha_venta.strftime('%Y%m%d')}{venta.id:04d}"
        venta.save()
        
        # Agregar items a la venta
        num_items = random.randint(1, 3)
        productos_venta = random.sample(list(productos), min(num_items, len(productos)))
        
        for producto in productos_venta:
            cantidad = random.randint(1, 2)
            precio_unitario = producto.precio
            
            ItemVenta.objects.create(
                venta=venta,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=precio_unitario
            )
        
        venta.calcular_totales()
        venta.save()
        
        ventas_creadas += 1
        print(f"Venta creada: {venta.numero_venta} - ${venta.total:,.0f} CLP - {venta.fecha_venta.date()}")
    
    print(f"Total ventas creadas para hoy: {ventas_creadas}")
    return ventas_creadas

def verificar_estadisticas_locales():
    """Verifica las estadísticas locales"""
    print("\n=== VERIFICACIÓN DE ESTADÍSTICAS LOCALES ===")
    
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
    print("=== CREANDO VENTAS LOCALES PARA HOY ===")
    print()
    
    try:
        # Crear ventas locales para hoy
        ventas_creadas = crear_ventas_locales_hoy()
        
        # Verificar estadísticas
        stats = verificar_estadisticas_locales()
        
        print(f"\n=== RESUMEN FINAL ===")
        print(f"✅ Se crearon {ventas_creadas} ventas para hoy")
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
        print(f"Error al crear ventas locales: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()
