#!/usr/bin/env python
"""
Script para inicializar el sistema de gestión de ventas del bazar
"""
import os
import sys
import django
from decimal import Decimal

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyectoVerduleriaVictorMondaca.settings')
django.setup()

from apps.auth_app.models import Usuario
from apps.djangoVer.models import Productos, Clientes

def init_system():
    """Inicializar el sistema con datos de prueba"""
    
    print("🚀 Inicializando sistema de gestión de ventas del bazar...")
    
    # 1. Crear usuarios de prueba
    print("\n👥 Creando usuarios de prueba...")
    
    # Vendedor
    vendedor, created = Usuario.objects.get_or_create(
        username='vendedor1',
        defaults={
            'email': 'vendedor1@bazar.com',
            'first_name': 'Juan',
            'last_name': 'Pérez',
            'rol': 'vendedor',
            'is_active': True
        }
    )
    if created:
        vendedor.set_password('vendedor123')
        vendedor.save()
        print("✅ Vendedor creado: vendedor1 / vendedor123")
    else:
        print("ℹ️  Vendedor ya existe")
    
    # Jefe de ventas
    jefe, created = Usuario.objects.get_or_create(
        username='jefe1',
        defaults={
            'email': 'jefe1@bazar.com',
            'first_name': 'María',
            'last_name': 'González',
            'rol': 'jefe_ventas',
            'is_active': True
        }
    )
    if created:
        jefe.set_password('jefe123')
        jefe.save()
        print("✅ Jefe de ventas creado: jefe1 / jefe123")
    else:
        print("ℹ️  Jefe de ventas ya existe")
    
    # 2. Crear productos de ejemplo con precios en pesos chilenos
    print("\n📦 Creando productos de ejemplo...")
    
    productos_data = [
        {'nombre': 'Manzanas', 'precio': Decimal('1200'), 'stock': 50, 'categoria': 'Frutas'},
        {'nombre': 'Plátanos', 'precio': Decimal('800'), 'stock': 30, 'categoria': 'Frutas'},
        {'nombre': 'Naranjas', 'precio': Decimal('1000'), 'stock': 40, 'categoria': 'Frutas'},
        {'nombre': 'Lechuga', 'precio': Decimal('600'), 'stock': 25, 'categoria': 'Verduras'},
        {'nombre': 'Tomates', 'precio': Decimal('1500'), 'stock': 35, 'categoria': 'Verduras'},
        {'nombre': 'Cebollas', 'precio': Decimal('900'), 'stock': 20, 'categoria': 'Verduras'},
        {'nombre': 'Papas', 'precio': Decimal('700'), 'stock': 60, 'categoria': 'Verduras'},
        {'nombre': 'Zanahorias', 'precio': Decimal('800'), 'stock': 45, 'categoria': 'Verduras'},
        {'nombre': 'Pan', 'precio': Decimal('1200'), 'stock': 30, 'categoria': 'Panadería'},
        {'nombre': 'Leche', 'precio': Decimal('1000'), 'stock': 25, 'categoria': 'Lácteos'},
    ]
    
    for producto_data in productos_data:
        producto, created = Productos.objects.get_or_create(
            nombre=producto_data['nombre'],
            defaults={
                'precio': producto_data['precio'],
                'stock': producto_data['stock'],
                'categoria': producto_data['categoria'],
                'descripcion': f"Producto fresco de {producto_data['categoria'].lower()}",
                'estado': 'disponible',
                'proveedor': 'Proveedor Local'
            }
        )
        if created:
            print(f"✅ Producto creado: {producto.nombre} - ${producto.precio} CLP")
        else:
            print(f"ℹ️  Producto ya existe: {producto.nombre}")
    
    # 3. Crear clientes de ejemplo con datos chilenos
    print("\n👤 Creando clientes de ejemplo...")
    
    clientes_data = [
        {
            'nombre': 'Ana García Silva', 
            'rut': '12.345.678-9', 
            'email': 'ana.garcia@email.com', 
            'telefono': '+56 9 1234 5678',
            'direccion': 'Av. Libertador Bernardo O\'Higgins 123',
            'comuna': 'Santiago',
            'tipo_cliente': 'consumidor_final',
            'tipo_persona': 'natural'
        },
        {
            'nombre': 'Carlos López Pérez', 
            'rut': '98.765.432-1', 
            'email': 'carlos.lopez@email.com', 
            'telefono': '+56 9 8765 4321',
            'direccion': 'Calle Las Flores 456',
            'comuna': 'Providencia',
            'tipo_cliente': 'contribuyente',
            'tipo_persona': 'natural'
        },
        {
            'nombre': 'Restaurante El Buen Sabor', 
            'rut': '76.543.210-K', 
            'email': 'contacto@buensabor.cl', 
            'telefono': '+56 2 2345 6789',
            'direccion': 'Av. Providencia 789',
            'comuna': 'Providencia',
            'tipo_cliente': 'empresa',
            'tipo_persona': 'juridica',
            'giro': 'Restaurante',
            'contacto': 'María Rodríguez'
        },
        {
            'nombre': 'Pedro Martínez González', 
            'rut': '11.222.333-4', 
            'email': 'pedro.martinez@email.com', 
            'telefono': '+56 9 3456 7890',
            'direccion': 'Pasaje Los Robles 321',
            'comuna': 'Las Condes',
            'tipo_cliente': 'consumidor_final',
            'tipo_persona': 'natural'
        },
    ]
    
    for cliente_data in clientes_data:
        cliente, created = Clientes.objects.get_or_create(
            rut=cliente_data['rut'],
            defaults=cliente_data
        )
        if created:
            print(f"✅ Cliente creado: {cliente.nombre} - {cliente.rut}")
        else:
            print(f"ℹ️  Cliente ya existe: {cliente.nombre}")
    
    print("\n🎉 Sistema inicializado exitosamente!")
    print("\n📋 Credenciales de acceso:")
    print("👤 Vendedor: vendedor1 / vendedor123")
    print("👑 Jefe de Ventas: jefe1 / jefe123")
    print("\n🌐 Acceder al sistema en: http://localhost:8000/auth/login/")

if __name__ == '__main__':
    try:
        init_system()
    except Exception as e:
        print(f"❌ Error al inicializar el sistema: {e}")
        sys.exit(1)
