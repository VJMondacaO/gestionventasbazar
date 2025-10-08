#!/usr/bin/env python3
"""
Script para crear datos de prueba para el resumen diario
Genera ventas, productos y clientes para probar el dashboard
"""

import os
import sys
import django
from datetime import datetime, timedelta, date
import random
from decimal import Decimal

# Configurar Django
sys.path.append('/Users/cazusin/Documents/Ingenieria de Software/Aplicacion/gestionVentasBazar')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestionVentasBazar.settings')
django.setup()

from apps.auth_app.models import Usuario
from apps.djangoVer.models import Productos, Clientes
from apps.ventas_app.models import Venta, ItemVenta
from django.db import transaction
from django.db.models import Sum

def crear_productos():
    """Crear productos de prueba"""
    productos_data = [
        {'nombre': 'Laptop HP Pavilion', 'precio': 450000, 'stock': 15, 'categoria': 'Electrónicos'},
        {'nombre': 'Mouse Inalámbrico', 'precio': 25000, 'stock': 50, 'categoria': 'Accesorios'},
        {'nombre': 'Teclado Mecánico', 'precio': 85000, 'stock': 30, 'categoria': 'Accesorios'},
        {'nombre': 'Monitor 24"', 'precio': 180000, 'stock': 20, 'categoria': 'Monitores'},
        {'nombre': 'Auriculares Bluetooth', 'precio': 65000, 'stock': 40, 'categoria': 'Audio'},
        {'nombre': 'Webcam HD', 'precio': 45000, 'stock': 25, 'categoria': 'Accesorios'},
        {'nombre': 'Tablet Samsung', 'precio': 320000, 'stock': 12, 'categoria': 'Electrónicos'},
        {'nombre': 'Cargador USB-C', 'precio': 15000, 'stock': 60, 'categoria': 'Accesorios'},
        {'nombre': 'Disco Duro 1TB', 'precio': 120000, 'stock': 18, 'categoria': 'Almacenamiento'},
        {'nombre': 'Memoria RAM 8GB', 'precio': 75000, 'stock': 35, 'categoria': 'Componentes'},
    ]
    
    productos_creados = []
    for producto_data in productos_data:
        producto, created = Productos.objects.get_or_create(
            nombre=producto_data['nombre'],
            defaults={
                'precio': producto_data['precio'],
                'stock': producto_data['stock'],
                'categoria': producto_data['categoria']
            }
        )
        productos_creados.append(producto)
        if created:
            print(f"✅ Producto creado: {producto.nombre}")
        else:
            print(f"ℹ️  Producto ya existe: {producto.nombre}")
    
    return productos_creados

def crear_clientes():
    """Crear clientes de prueba"""
    clientes_data = [
        {'nombre': 'Juan Pérez', 'rut': '12.345.678-9', 'email': 'juan.perez@email.com', 'telefono': '+56912345678'},
        {'nombre': 'María González', 'rut': '98.765.432-1', 'email': 'maria.gonzalez@email.com', 'telefono': '+56987654321'},
        {'nombre': 'Carlos López', 'rut': '11.222.333-4', 'email': 'carlos.lopez@email.com', 'telefono': '+56911223344'},
        {'nombre': 'Ana Martínez', 'rut': '55.666.777-8', 'email': 'ana.martinez@email.com', 'telefono': '+56955667788'},
        {'nombre': 'Pedro Rodríguez', 'rut': '99.888.777-6', 'email': 'pedro.rodriguez@email.com', 'telefono': '+56999887766'},
        {'nombre': 'Laura Sánchez', 'rut': '44.333.222-1', 'email': 'laura.sanchez@email.com', 'telefono': '+56944332211'},
        {'nombre': 'Miguel Torres', 'rut': '77.889.900-3', 'email': 'miguel.torres@email.com', 'telefono': '+56977889900'},
        {'nombre': 'Cliente General', 'rut': '00.000.000-0', 'email': 'general@bazar.com', 'telefono': '+56900000000'},
    ]
    
    clientes_creados = []
    for cliente_data in clientes_data:
        try:
            cliente, created = Clientes.objects.get_or_create(
                rut=cliente_data['rut'],
                defaults={
                    'nombre': cliente_data['nombre'],
                    'email': cliente_data['email'],
                    'telefono': cliente_data['telefono'],
                    'direccion': 'Dirección de prueba',
                    'comuna': 'Santiago',
                    'region': 'Metropolitana'
                }
            )
            clientes_creados.append(cliente)
            if created:
                print(f"✅ Cliente creado: {cliente.nombre}")
            else:
                print(f"ℹ️  Cliente ya existe: {cliente.nombre}")
        except Exception as e:
            print(f"❌ Error creando cliente {cliente_data['nombre']}: {e}")
            # Si hay error, usar cliente general existente
            try:
                cliente_general = Clientes.objects.get(nombre='Cliente General')
                clientes_creados.append(cliente_general)
            except:
                pass
    
    return clientes_creados

def crear_ventas_hoy(productos, clientes, vendedor):
    """Crear ventas para hoy"""
    hoy = date.today()
    ventas_creadas = []
    
    # Crear 8-12 ventas para hoy
    num_ventas = random.randint(8, 12)
    
    for i in range(num_ventas):
        with transaction.atomic():
            # Crear venta
            venta = Venta.objects.create(
                numero_venta=f"V-{hoy.strftime('%Y%m%d')}-{i+1:03d}",
                vendedor=vendedor,
                cliente=random.choice(clientes),
                fecha_venta=datetime.now() - timedelta(hours=random.randint(0, 8)),
                estado='completada',
                subtotal=0,
                iva=0,
                total=0
            )
            
            # Agregar items a la venta
            num_items = random.randint(1, 4)
            productos_venta = random.sample(productos, min(num_items, len(productos)))
            
            subtotal = 0
            for producto in productos_venta:
                cantidad = random.randint(1, 3)
                precio_unitario = producto.precio
                subtotal_item = cantidad * precio_unitario
                
                ItemVenta.objects.create(
                    venta=venta,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=precio_unitario,
                    subtotal=subtotal_item
                )
                
                subtotal += subtotal_item
                # Reducir stock
                producto.stock = max(0, producto.stock - cantidad)
                producto.save()
            
            # Calcular totales
            iva = subtotal * Decimal('0.19')  # 19% IVA
            total = subtotal + iva
            
            venta.subtotal = subtotal
            venta.iva = iva
            venta.total = total
            venta.save()
            
            ventas_creadas.append(venta)
            print(f"✅ Venta creada: {venta.numero_venta} - ${total:,.0f}")
    
    return ventas_creadas

def crear_ventas_mes_actual(productos, clientes, vendedor):
    """Crear ventas para el mes actual"""
    hoy = date.today()
    inicio_mes = hoy.replace(day=1)
    ventas_creadas = []
    
    # Crear ventas distribuidas en el mes
    dias_mes = (hoy - inicio_mes).days + 1
    ventas_por_dia = max(1, 15 // dias_mes)  # Distribuir ~15 ventas en el mes
    
    for dia in range(dias_mes):
        fecha_venta = inicio_mes + timedelta(days=dia)
        if fecha_venta == hoy:
            continue  # Ya creamos las ventas de hoy
        
        num_ventas_dia = random.randint(0, ventas_por_dia)
        
        for i in range(num_ventas_dia):
            with transaction.atomic():
                venta = Venta.objects.create(
                    numero_venta=f"V-{fecha_venta.strftime('%Y%m%d')}-{i+1:03d}",
                    vendedor=vendedor,
                    cliente=random.choice(clientes),
                    fecha_venta=datetime.combine(fecha_venta, datetime.min.time()) + timedelta(hours=random.randint(9, 18)),
                    estado='completada',
                    subtotal=0,
                    iva=0,
                    total=0
                )
                
                # Agregar items
                num_items = random.randint(1, 3)
                productos_venta = random.sample(productos, min(num_items, len(productos)))
                
                subtotal = 0
                for producto in productos_venta:
                    cantidad = random.randint(1, 2)
                    precio_unitario = producto.precio
                    subtotal_item = cantidad * precio_unitario
                    
                    ItemVenta.objects.create(
                        venta=venta,
                        producto=producto,
                        cantidad=cantidad,
                        precio_unitario=precio_unitario,
                        subtotal=subtotal_item
                    )
                    
                    subtotal += subtotal_item
                    # Reducir stock
                    producto.stock = max(0, producto.stock - cantidad)
                    producto.save()
                
                # Calcular totales
                iva = subtotal * Decimal('0.19')
                total = subtotal + iva
                
                venta.subtotal = subtotal
                venta.iva = iva
                venta.total = total
                venta.save()
                
                ventas_creadas.append(venta)
                print(f"✅ Venta del mes creada: {venta.numero_venta} - ${total:,.0f}")
    
    return ventas_creadas

def verificar_estadisticas():
    """Verificar las estadísticas generadas"""
    hoy = date.today()
    inicio_mes = hoy.replace(day=1)
    
    # Estadísticas de hoy
    ventas_hoy = Venta.objects.filter(fecha_venta__date=hoy, estado='completada')
    total_ventas_hoy = ventas_hoy.count()
    total_dinero_hoy = ventas_hoy.aggregate(Sum('total'))['total__sum'] or 0
    
    # Estadísticas del mes
    ventas_mes = Venta.objects.filter(
        fecha_venta__date__gte=inicio_mes,
        estado='completada'
    )
    total_ventas_mes = ventas_mes.count()
    total_dinero_mes = ventas_mes.aggregate(Sum('total'))['total__sum'] or 0
    
    print(f"\n📊 ESTADÍSTICAS GENERADAS:")
    print(f"   Ventas Hoy: {total_ventas_hoy}")
    print(f"   Ingresos Hoy: ${total_dinero_hoy:,.0f} CLP")
    print(f"   Ventas del Mes: {total_ventas_mes}")
    print(f"   Ingresos del Mes: ${total_dinero_mes:,.0f} CLP")
    
    # Productos con stock bajo
    productos_stock_bajo = Productos.objects.filter(stock__lt=10).count()
    print(f"   Productos con Stock Bajo: {productos_stock_bajo}")

def main():
    """Función principal"""
    print("🚀 Creando datos de prueba para el resumen diario...")
    
    # Obtener o crear vendedor
    try:
        vendedor = Usuario.objects.get(username='vendedor1')
        print(f"✅ Usuario vendedor encontrado: {vendedor.username}")
    except Usuario.DoesNotExist:
        print("❌ Usuario vendedor1 no encontrado. Creando...")
        vendedor = Usuario.objects.create_user(
            username='vendedor1',
            email='vendedor1@bazar.com',
            password='vendedor123',
            first_name='Vendedor',
            last_name='Uno',
            rol='vendedor'
        )
        print(f"✅ Usuario vendedor creado: {vendedor.username}")
    
    # Crear productos
    print("\n📦 Creando productos...")
    productos = crear_productos()
    
    # Crear clientes
    print("\n👥 Creando clientes...")
    clientes = crear_clientes()
    
    # Crear ventas de hoy
    print("\n💰 Creando ventas para hoy...")
    ventas_hoy = crear_ventas_hoy(productos, clientes, vendedor)
    
    # Crear ventas del mes
    print("\n📅 Creando ventas del mes actual...")
    ventas_mes = crear_ventas_mes_actual(productos, clientes, vendedor)
    
    # Verificar estadísticas
    verificar_estadisticas()
    
    print(f"\n✅ ¡Datos de prueba creados exitosamente!")
    print(f"   - {len(productos)} productos")
    print(f"   - {len(clientes)} clientes")
    print(f"   - {len(ventas_hoy)} ventas de hoy")
    print(f"   - {len(ventas_mes)} ventas del mes")
    print(f"\n🌐 Accede al sistema en: http://127.0.0.1:8000/")
    print(f"   Usuario: vendedor1")
    print(f"   Contraseña: vendedor123")

if __name__ == '__main__':
    main()
