#!/usr/bin/env python3
"""
Script simplificado para crear datos de prueba básicos para el sistema de gestión de ventas del bazar.
"""

import os
import sys
import django
from datetime import datetime, timedelta
import random

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestionVentasBazar.settings')
django.setup()

from apps.auth_app.models import Usuario
from apps.djangoVer.models import Productos, Clientes
from apps.ventas_app.models import Venta, ItemVenta, ControlDia

def crear_usuarios_adicionales():
    """Crea algunos usuarios adicionales"""
    print("Creando usuarios adicionales...")
    
    usuarios_adicionales = [
        ('vendedor21', 'María', 'González', 'maria@bazar.com'),
        ('vendedor22', 'Carlos', 'López', 'carlos@bazar.com'),
        ('vendedor23', 'Ana', 'Martín', 'ana@bazar.com'),
        ('vendedor24', 'Luis', 'Sánchez', 'luis@bazar.com'),
        ('vendedor25', 'Carmen', 'Pérez', 'carmen@bazar.com'),
    ]
    
    for username, nombre, apellido, email in usuarios_adicionales:
        if not Usuario.objects.filter(username=username).exists():
            usuario = Usuario.objects.create_user(
                username=username,
                email=email,
                password='vendedor123',
                first_name=nombre,
                last_name=apellido,
                is_staff=False,
                is_superuser=False
            )
            print(f"Usuario creado: {username} - {nombre} {apellido}")
        else:
            print(f"Usuario {username} ya existe")

def crear_productos_adicionales():
    """Crea algunos productos adicionales"""
    print("Creando productos adicionales...")
    
    productos_adicionales = [
        ('Aceitunas', 'Aceitunas verdes', 1500, 20, 'Conservas', 'disponible', 'Proveedor Sur'),
        ('Atún', 'Atún en lata', 2000, 15, 'Conservas', 'disponible', 'Proveedor Sur'),
        ('Café', 'Café molido 500g', 3000, 10, 'Bebidas', 'disponible', 'Proveedor Central'),
        ('Té', 'Té negro 100 bolsas', 2500, 8, 'Bebidas', 'disponible', 'Proveedor Central'),
        ('Galletas', 'Galletas surtidas', 1200, 25, 'Dulces', 'disponible', 'Proveedor Central'),
    ]
    
    for nombre, descripcion, precio, stock, categoria, estado, proveedor in productos_adicionales:
        if not Productos.objects.filter(nombre=nombre).exists():
            producto = Productos.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                stock=stock,
                categoria=categoria,
                estado=estado,
                proveedor=proveedor
            )
            print(f"Producto creado: {nombre} - ${precio}")
        else:
            print(f"Producto {nombre} ya existe")

def crear_clientes_adicionales():
    """Crea algunos clientes adicionales"""
    print("Creando clientes adicionales...")
    
    clientes_adicionales = [
        ('Juan Pérez', '12.345.678-9', 'juan@email.com', '+56912345678', 'Av. Principal 123', 'Santiago', 'Metropolitana'),
        ('María González', '98.765.432-1', 'maria@email.com', '+56987654321', 'Calle Secundaria 456', 'Las Condes', 'Metropolitana'),
        ('Carlos López', '11.222.333-4', 'carlos@email.com', '+56911223334', 'Pasaje Norte 789', 'Providencia', 'Metropolitana'),
        ('Ana Martín', '55.666.777-8', 'ana@email.com', '+56955666777', 'Av. Sur 321', 'Ñuñoa', 'Metropolitana'),
        ('Luis Sánchez', '99.888.777-6', 'luis@email.com', '+56999888777', 'Calle Este 654', 'Maipú', 'Metropolitana'),
    ]
    
    for nombre, rut, email, telefono, direccion, comuna, region in clientes_adicionales:
        if not Clientes.objects.filter(rut=rut).exists():
            cliente = Clientes.objects.create(
                nombre=nombre,
                rut=rut,
                email=email,
                telefono=telefono,
                direccion=direccion,
                comuna=comuna,
                region=region,
                tipo_cliente='consumidor_final'
            )
            print(f"Cliente creado: {nombre} - {rut}")
        else:
            print(f"Cliente {nombre} ya existe")

def crear_ventas_simples():
    """Crea algunas ventas simples"""
    print("Creando ventas simples...")
    
    vendedores = Usuario.objects.filter(username__startswith='vendedor')[:3]
    clientes = Clientes.objects.all()[:5]
    productos = Productos.objects.all()[:10]
    
    for i in range(10):
        vendedor = random.choice(vendedores)
        cliente = random.choice(clientes)
        tipo_documento = random.choice(['boleta', 'factura'])
        forma_pago = random.choice(['efectivo', 'transferencia'])
        
        venta = Venta.objects.create(
            vendedor=vendedor,
            cliente=cliente,
            tipo_documento=tipo_documento,
            forma_pago=forma_pago,
            estado='completada',
            fecha_venta=datetime.now() - timedelta(days=random.randint(1, 7))
        )
        
        # Generar número de venta único
        venta.numero_venta = f"V{datetime.now().strftime('%Y%m%d')}{venta.id:04d}"
        venta.save()
        
        # Agregar items a la venta
        num_items = random.randint(1, 3)
        productos_venta = random.sample(list(productos), num_items)
        
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
        
        print(f"Venta creada: {venta.numero_venta} - {vendedor.username} - ${venta.total}")

def main():
    """Función principal"""
    print("=== CREANDO DATOS DE PRUEBA SIMPLES ===")
    print()
    
    try:
        # Crear usuarios adicionales
        crear_usuarios_adicionales()
        print()
        
        # Crear productos adicionales
        crear_productos_adicionales()
        print()
        
        # Crear clientes adicionales
        crear_clientes_adicionales()
        print()
        
        # Crear ventas simples
        crear_ventas_simples()
        print()
        
        print("=== DATOS DE PRUEBA CREADOS EXITOSAMENTE ===")
        print("Se han creado usuarios, productos, clientes y ventas adicionales")
        
    except Exception as e:
        print(f"Error al crear datos de prueba: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()
