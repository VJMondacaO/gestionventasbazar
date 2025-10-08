#!/usr/bin/env python3
"""
Script final para crear datos de prueba para el sistema de gestión de ventas del bazar.
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

def crear_usuarios_finales():
    """Crea usuarios finales para pruebas"""
    print("Creando usuarios finales...")
    
    # Crear algunos vendedores adicionales
    for i in range(26, 31):
        nombre = f"Vendedor{i}"
        username = f"vendedor{i}"
        email = f"vendedor{i}@bazar.com"
        
        if not Usuario.objects.filter(username=username).exists():
            usuario = Usuario.objects.create_user(
                username=username,
                email=email,
                password='vendedor123',
                first_name=nombre,
                last_name='Apellido',
                is_staff=False,
                is_superuser=False
            )
            print(f"Usuario creado: {username}")

def crear_productos_finales():
    """Crea productos finales para pruebas"""
    print("Creando productos finales...")
    
    productos_finales = [
        ('Yogurt', 'Yogurt natural', 800, 30, 'Lácteos', 'disponible', 'Proveedor Lácteos'),
        ('Mantequilla', 'Mantequilla 200g', 1500, 20, 'Lácteos', 'disponible', 'Proveedor Lácteos'),
        ('Cereal', 'Cereal de avena', 2500, 15, 'Cereales', 'disponible', 'Proveedor Central'),
        ('Miel', 'Miel natural 500g', 3000, 10, 'Endulzantes', 'disponible', 'Proveedor Central'),
        ('Vinagre', 'Vinagre blanco 500ml', 800, 25, 'Condimentos', 'disponible', 'Proveedor Central'),
    ]
    
    for nombre, descripcion, precio, stock, categoria, estado, proveedor in productos_finales:
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

def crear_clientes_finales():
    """Crea clientes finales para pruebas"""
    print("Creando clientes finales...")
    
    clientes_finales = [
        ('Roberto Silva', '13.456.789-0', 'roberto@email.com', '+56912345678', 'Av. Libertador 123', 'Santiago', 'Metropolitana'),
        ('Patricia Torres', '14.567.890-1', 'patricia@email.com', '+56923456789', 'Calle Independencia 456', 'Las Condes', 'Metropolitana'),
        ('Miguel Herrera', '15.678.901-2', 'miguel@email.com', '+56934567890', 'Pasaje República 789', 'Providencia', 'Metropolitana'),
        ('Isabel Morales', '16.789.012-3', 'isabel@email.com', '+56945678901', 'Av. Constitución 321', 'Ñuñoa', 'Metropolitana'),
        ('Fernando Castro', '17.890.123-4', 'fernando@email.com', '+56956789012', 'Calle Norte 654', 'Maipú', 'Metropolitana'),
    ]
    
    for nombre, rut, email, telefono, direccion, comuna, region in clientes_finales:
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

def crear_ventas_finales():
    """Crea ventas finales para pruebas"""
    print("Creando ventas finales...")
    
    vendedores = Usuario.objects.filter(username__startswith='vendedor')[:3]
    clientes = Clientes.objects.all()[:5]
    productos = Productos.objects.all()[:10]
    
    for i in range(5):
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
            fecha_venta=datetime.now() - timedelta(days=random.randint(1, 3))
        )
        
        # Generar número de venta único
        venta.numero_venta = f"V{datetime.now().strftime('%Y%m%d')}{venta.id:04d}"
        venta.save()
        
        # Agregar items a la venta
        num_items = random.randint(1, 2)
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
    print("=== CREANDO DATOS DE PRUEBA FINALES ===")
    print()
    
    try:
        # Crear usuarios finales
        crear_usuarios_finales()
        print()
        
        # Crear productos finales
        crear_productos_finales()
        print()
        
        # Crear clientes finales
        crear_clientes_finales()
        print()
        
        # Crear ventas finales
        crear_ventas_finales()
        print()
        
        print("=== DATOS DE PRUEBA FINALES CREADOS EXITOSAMENTE ===")
        print("Se han creado usuarios, productos, clientes y ventas finales")
        print()
        print("Usuarios de prueba disponibles:")
        print("- vendedor1 a vendedor30 (contraseña: vendedor123)")
        print("- jefe1 a jefe5 (contraseña: jefe123)")
        
    except Exception as e:
        print(f"Error al crear datos de prueba: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()
