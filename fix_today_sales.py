#!/usr/bin/env python3
"""
Script para corregir las ventas de hoy y crear nuevas ventas con la fecha correcta.
"""

import os
import sys
import django
from datetime import datetime, timedelta
import random
from django.utils import timezone

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestionVentasBazar.settings')
django.setup()

from apps.auth_app.models import Usuario
from apps.djangoVer.models import Productos, Clientes
from apps.ventas_app.models import Venta, ItemVenta

def corregir_ventas_hoy():
    """Corrige las ventas de hoy para que tengan la fecha correcta"""
    print("Corrigiendo ventas de hoy...")
    
    # Obtener ventas de mañana (que deberían ser de hoy)
    mañana = datetime.now().date() + timedelta(days=1)
    ventas_mañana = Venta.objects.filter(fecha_venta__date=mañana)
    
    print(f"Ventas encontradas para mañana: {ventas_mañana.count()}")
    
    # Corregir las fechas
    hoy = datetime.now().date()
    ventas_corregidas = 0
    
    for venta in ventas_mañana:
        # Crear nueva fecha para hoy con hora aleatoria
        hora_aleatoria = random.randint(8, 20)
        minuto_aleatorio = random.randint(0, 59)
        nueva_fecha = timezone.make_aware(
            datetime.combine(hoy, datetime.min.time().replace(hour=hora_aleatoria, minute=minuto_aleatorio))
        )
        
        venta.fecha_venta = nueva_fecha
        venta.save()
        ventas_corregidas += 1
        print(f"Venta {venta.numero_venta} corregida a {nueva_fecha}")
    
    print(f"Total ventas corregidas: {ventas_corregidas}")
    return ventas_corregidas

def crear_mas_ventas_hoy():
    """Crea más ventas para hoy"""
    print("Creando más ventas para hoy...")
    
    # Obtener vendedores y productos
    vendedores = Usuario.objects.filter(username__startswith='vendedor')[:5]
    clientes = Clientes.objects.all()
    productos = Productos.objects.all()
    
    # Crear ventas para hoy
    hoy = datetime.now().date()
    ventas_creadas = 0
    
    for i in range(5):  # Crear 5 ventas más para hoy
        # Hora aleatoria de hoy
        hora_aleatoria = random.randint(8, 20)  # Entre 8 AM y 8 PM
        minuto_aleatorio = random.randint(0, 59)
        fecha_venta = timezone.make_aware(
            datetime.combine(hoy, datetime.min.time().replace(hour=hora_aleatoria, minute=minuto_aleatorio))
        )
        
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
        num_items = random.randint(1, 4)
        productos_venta = random.sample(list(productos), min(num_items, len(productos)))
        
        for producto in productos_venta:
            cantidad = random.randint(1, 3)
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
        print(f"Venta creada: {venta.numero_venta} - ${venta.total:,.0f} CLP")
    
    print(f"Total ventas creadas para hoy: {ventas_creadas}")
    return ventas_creadas

def verificar_estadisticas_hoy():
    """Verifica las estadísticas de hoy"""
    print("\n=== VERIFICACIÓN DE ESTADÍSTICAS DE HOY ===")
    
    hoy = datetime.now().date()
    
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
    print("=== CORRIGIENDO VENTAS DE HOY ===")
    print()
    
    try:
        # Corregir ventas existentes
        ventas_corregidas = corregir_ventas_hoy()
        
        # Crear más ventas para hoy
        ventas_creadas = crear_mas_ventas_hoy()
        
        # Verificar estadísticas
        stats = verificar_estadisticas_hoy()
        
        print(f"\n=== RESUMEN ===")
        print(f"✅ Se corrigieron {ventas_corregidas} ventas")
        print(f"✅ Se crearon {ventas_creadas} ventas nuevas")
        print(f"✅ Las tarjetas del dashboard ahora deberían mostrar:")
        print(f"   - Ventas Hoy: {stats['ventas_hoy']}")
        print(f"   - Ingresos Hoy: ${stats['ingresos_hoy']:,.0f} CLP")
        print(f"   - Ventas Semana: {stats['ventas_semana']}")
        print(f"   - Ingresos Semana: ${stats['ingresos_semana']:,.0f} CLP")
        print(f"   - Ventas Mes: {stats['ventas_mes']}")
        print(f"   - Ingresos Mes: ${stats['ingresos_mes']:,.0f} CLP")
        
    except Exception as e:
        print(f"Error al corregir ventas de hoy: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()
