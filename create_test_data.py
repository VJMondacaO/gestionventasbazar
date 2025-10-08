#!/usr/bin/env python3
"""
Script para crear datos de prueba para el sistema de gestión de ventas del bazar.
Genera usuarios, productos y clientes con datos chilenos.
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
from django.contrib.auth.hashers import make_password

# Datos chilenos para generar información realista
NOMBRES_CHILENOS = [
    'Alejandro', 'Andrés', 'Antonio', 'Carlos', 'Cristian', 'Daniel', 'Diego', 'Eduardo', 'Fernando', 'Francisco',
    'Gabriel', 'Gonzalo', 'Héctor', 'Ignacio', 'Javier', 'Jorge', 'José', 'Juan', 'Luis', 'Manuel',
    'María', 'Ana', 'Carmen', 'Claudia', 'Elena', 'Francisca', 'Isabel', 'Javiera', 'Katherine', 'Laura',
    'Lorena', 'Marcela', 'Natalia', 'Patricia', 'Paula', 'Rosa', 'Sandra', 'Sofía', 'Valentina', 'Verónica'
]

APELLIDOS_CHILENOS = [
    'González', 'Muñoz', 'Rojas', 'Díaz', 'Pérez', 'Soto', 'Contreras', 'Silva', 'Martínez', 'Sepúlveda',
    'Morales', 'Rodríguez', 'López', 'Fuentes', 'Hernández', 'Torres', 'Araya', 'Flores', 'Espinoza', 'Valenzuela',
    'Castillo', 'Ramírez', 'Reyes', 'Gutiérrez', 'Castro', 'Vargas', 'Álvarez', 'Vásquez', 'Tapia', 'Fernández',
    'Sánchez', 'Carrasco', 'Gómez', 'Cortés', 'Herrera', 'Núñez', 'Jiménez', 'Parra', 'Vera', 'Moreno'
]

PRODUCTOS_BAZAR = [
    ('Manzanas Rojas', 'Frutas frescas de temporada', 1200, 50, 'Frutas', 'disponible', 'Proveedor Norte'),
    ('Peras', 'Peras jugosas y dulces', 1500, 30, 'Frutas', 'disponible', 'Proveedor Norte'),
    ('Bananas', 'Bananas maduras y frescas', 800, 40, 'Frutas', 'disponible', 'Proveedor Norte'),
    ('Naranjas', 'Naranjas de jugo', 1000, 35, 'Frutas', 'disponible', 'Proveedor Norte'),
    ('Limones', 'Limones ácidos', 600, 25, 'Frutas', 'disponible', 'Proveedor Norte'),
    ('Tomates', 'Tomates frescos', 1800, 20, 'Verduras', 'disponible', 'Proveedor Sur'),
    ('Lechuga', 'Lechuga fresca', 500, 15, 'Verduras', 'disponible', 'Proveedor Sur'),
    ('Cebollas', 'Cebollas blancas', 700, 30, 'Verduras', 'disponible', 'Proveedor Sur'),
    ('Papas', 'Papas frescas', 900, 40, 'Verduras', 'disponible', 'Proveedor Sur'),
    ('Zanahorias', 'Zanahorias frescas', 800, 25, 'Verduras', 'disponible', 'Proveedor Sur'),
    ('Arroz 1kg', 'Arroz grano largo', 1200, 20, 'Granos', 'disponible', 'Proveedor Central'),
    ('Fideos', 'Fideos largos', 800, 30, 'Granos', 'disponible', 'Proveedor Central'),
    ('Azúcar 1kg', 'Azúcar blanca', 1000, 15, 'Endulzantes', 'disponible', 'Proveedor Central'),
    ('Sal 500g', 'Sal marina', 300, 20, 'Condimentos', 'disponible', 'Proveedor Central'),
    ('Aceite 1L', 'Aceite vegetal', 2500, 10, 'Aceites', 'disponible', 'Proveedor Central'),
    ('Leche 1L', 'Leche entera', 800, 25, 'Lácteos', 'disponible', 'Proveedor Lácteos'),
    ('Huevos x12', 'Huevos frescos', 1200, 20, 'Lácteos', 'disponible', 'Proveedor Lácteos'),
    ('Queso 200g', 'Queso gouda', 2000, 15, 'Lácteos', 'disponible', 'Proveedor Lácteos'),
    ('Jamón 200g', 'Jamón cocido', 1800, 12, 'Carnes', 'disponible', 'Proveedor Carnes'),
    ('Pan', 'Pan fresco', 500, 30, 'Panadería', 'disponible', 'Proveedor Panadería')
]

COMUNAS_CHILE = [
    'Santiago', 'Las Condes', 'Providencia', 'Ñuñoa', 'Maipú', 'Puente Alto', 'La Florida', 'San Bernardo',
    'Valparaíso', 'Viña del Mar', 'Concepción', 'Temuco', 'Antofagasta', 'Iquique', 'Arica', 'La Serena',
    'Coquimbo', 'Rancagua', 'Talca', 'Chillán', 'Osorno', 'Puerto Montt', 'Punta Arenas'
]

REGIONES_CHILE = [
    'Metropolitana', 'Valparaíso', 'Biobío', 'Araucanía', 'Antofagasta', 'Tarapacá', 'Arica y Parinacota',
    'Coquimbo', 'O\'Higgins', 'Maule', 'Ñuble', 'Los Lagos', 'Magallanes'
]

def generar_rut():
    """Genera un RUT chileno válido"""
    numero = random.randint(1000000, 25000000)
    dv = calcular_dv(numero)
    return f"{numero:,}".replace(',', '.') + f"-{dv}"

def calcular_dv(numero):
    """Calcula el dígito verificador de un RUT chileno"""
    rut = str(numero)
    suma = 0
    multiplicador = 2
    
    for i in reversed(rut):
        suma += int(i) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2
    
    resto = suma % 11
    dv = 11 - resto
    if dv == 11:
        return '0'
    elif dv == 10:
        return 'K'
    else:
        return str(dv)

def crear_usuarios():
    """Crea usuarios de prueba"""
    print("Creando usuarios de prueba...")
    
    # Crear algunos vendedores
    for i in range(1, 21):
        nombre = random.choice(NOMBRES_CHILENOS)
        apellido = random.choice(APELLIDOS_CHILENOS)
        username = f"vendedor{i}"
        email = f"vendedor{i}@bazar.com"
        
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
    
    # Crear algunos jefes de ventas
    for i in range(1, 6):
        nombre = random.choice(NOMBRES_CHILENOS)
        apellido = random.choice(APELLIDOS_CHILENOS)
        username = f"jefe{i}"
        email = f"jefe{i}@bazar.com"
        
        if not Usuario.objects.filter(username=username).exists():
            usuario = Usuario.objects.create_user(
                username=username,
                email=email,
                password='jefe123',
                first_name=nombre,
                last_name=apellido,
                is_staff=True,
                is_superuser=False
            )
            print(f"Jefe creado: {username} - {nombre} {apellido}")
        else:
            print(f"Jefe {username} ya existe")

def crear_productos():
    """Crea productos de prueba"""
    print("Creando productos de prueba...")
    
    for nombre, descripcion, precio, stock, categoria, estado, proveedor in PRODUCTOS_BAZAR:
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

def crear_clientes():
    """Crea clientes de prueba"""
    print("Creando clientes de prueba...")
    
    tipos_cliente = ['Consumidor Final', 'Contribuyente', 'Empresa']
    
    for i in range(100):
        nombre = random.choice(NOMBRES_CHILENOS)
        apellido = random.choice(APELLIDOS_CHILENOS)
        rut = generar_rut()
        email = f"{nombre.lower()}.{apellido.lower()}@email.com"
        telefono = f"+569{random.randint(10000000, 99999999)}"
        direccion = f"{random.choice(['Av.', 'Calle', 'Pasaje'])} {random.choice(['Libertador', 'Independencia', 'República', 'Constitución'])} #{random.randint(100, 9999)}"
        comuna = random.choice(COMUNAS_CHILE)
        region = random.choice(REGIONES_CHILE)
        tipo_cliente = random.choice(tipos_cliente)
        
        cliente = Clientes.objects.create(
            nombre=f"{nombre} {apellido}",
            rut=rut,
            email=email,
            telefono=telefono,
            direccion=direccion,
            comuna=comuna,
            region=region,
            tipo_cliente=tipo_cliente
        )
        print(f"Cliente creado: {nombre} {apellido} - {rut}")

def crear_ventas_ejemplo():
    """Crea algunas ventas de ejemplo"""
    print("Creando ventas de ejemplo...")
    
    vendedores = Usuario.objects.filter(username__startswith='vendedor')[:5]
    clientes = Clientes.objects.all()[:20]
    productos = Productos.objects.all()
    
    for i in range(50):
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
            fecha_venta=datetime.now() - timedelta(days=random.randint(1, 30))
        )
        
        # Generar número de venta único
        fecha_actual = datetime.now()
        venta.numero_venta = f"V{fecha_actual.strftime('%Y%m%d')}{venta.id:04d}"
        venta.save()
        
        # Agregar items a la venta
        num_items = random.randint(1, 5)
        productos_venta = random.sample(list(productos), num_items)
        
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
        
        print(f"Venta creada: {venta.numero_venta} - {vendedor.username} - ${venta.total}")

def crear_control_dia():
    """Crea control de día para hoy"""
    print("Creando control de día...")
    
    hoy = datetime.now().date()
    jefe = Usuario.objects.filter(username__startswith='jefe').first()
    
    if jefe:
        control_dia = ControlDia.objects.create(
            fecha=hoy,
            estado='abierto',
            usuario_apertura=jefe
        )
        print(f"Control de día creado para {hoy}")

def main():
    """Función principal"""
    print("=== CREANDO DATOS DE PRUEBA PARA EL BAZAR ===")
    print("Este script creará usuarios, productos, clientes y ventas de ejemplo")
    print()
    
    try:
        # Crear usuarios
        crear_usuarios()
        print()
        
        # Crear productos
        crear_productos()
        print()
        
        # Crear clientes
        crear_clientes()
        print()
        
        # Crear ventas de ejemplo
        crear_ventas_ejemplo()
        print()
        
        # Crear control de día
        crear_control_dia()
        print()
        
        print("=== DATOS DE PRUEBA CREADOS EXITOSAMENTE ===")
        print("Usuarios de prueba:")
        print("- vendedor1 a vendedor20 (contraseña: vendedor123)")
        print("- jefe1 a jefe5 (contraseña: jefe123)")
        print()
        print("Se han creado 100 clientes, 20 productos y 50 ventas de ejemplo")
        
    except Exception as e:
        print(f"Error al crear datos de prueba: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()
