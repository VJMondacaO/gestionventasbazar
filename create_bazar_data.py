#!/usr/bin/env python3
"""
Script para crear datos masivos del bazar chileno con productos típicos y ventas históricas.
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

# Productos típicos de bazar en Chile
PRODUCTOS_BAZAR_CHILE = [
    # Bebidas
    ('Coca Cola 500ml', 'Bebida gaseosa', 1200, 50, 'Bebidas', 'disponible', 'Proveedor Norte'),
    ('Agua Mineral 1L', 'Agua purificada', 800, 30, 'Bebidas', 'disponible', 'Proveedor Norte'),
    ('Jugo de Naranja 1L', 'Jugo natural', 1000, 40, 'Bebidas', 'disponible', 'Proveedor Norte'),
    ('Cerveza 350ml', 'Cerveza nacional', 1500, 25, 'Bebidas', 'disponible', 'Proveedor Norte'),
    ('Vino Tinto 750ml', 'Vino de mesa', 3000, 15, 'Bebidas', 'disponible', 'Proveedor Norte'),
    ('Energizante 250ml', 'Bebida energética', 2000, 20, 'Bebidas', 'disponible', 'Proveedor Norte'),
    ('Té en Bolsitas', 'Té negro', 500, 30, 'Bebidas', 'disponible', 'Proveedor Norte'),
    ('Café Instantáneo', 'Café soluble', 2500, 18, 'Bebidas', 'disponible', 'Proveedor Norte'),
    ('Chocolate en Polvo', 'Cacao en polvo', 1800, 12, 'Bebidas', 'disponible', 'Proveedor Norte'),
    ('Agua Saborizada', 'Agua con sabor', 1000, 25, 'Bebidas', 'disponible', 'Proveedor Norte'),
    
    # Panadería
    ('Pan de Molde', 'Pan blanco', 1200, 20, 'Panadería', 'disponible', 'Proveedor Sur'),
    ('Galletas Saladas', 'Galletas de agua', 800, 15, 'Panadería', 'disponible', 'Proveedor Sur'),
    ('Tortillas', 'Tortillas de harina', 1500, 30, 'Panadería', 'disponible', 'Proveedor Sur'),
    ('Cereales', 'Cereales de desayuno', 2500, 25, 'Cereales', 'disponible', 'Proveedor Sur'),
    ('Avena 500g', 'Avena natural', 1500, 20, 'Cereales', 'disponible', 'Proveedor Sur'),
    ('Galletas Dulces', 'Galletas de chocolate', 2000, 18, 'Panadería', 'disponible', 'Proveedor Sur'),
    ('Pan Integral', 'Pan de trigo integral', 1800, 15, 'Panadería', 'disponible', 'Proveedor Sur'),
    ('Tostadas', 'Pan tostado', 1000, 20, 'Panadería', 'disponible', 'Proveedor Sur'),
    ('Croissants', 'Croissants de mantequilla', 2500, 12, 'Panadería', 'disponible', 'Proveedor Sur'),
    ('Muffins', 'Muffins de chocolate', 3000, 10, 'Panadería', 'disponible', 'Proveedor Sur'),
    
    # Granos y Cereales
    ('Arroz 1kg', 'Arroz grano largo', 1200, 20, 'Granos', 'disponible', 'Proveedor Central'),
    ('Fideos', 'Fideos largos', 800, 30, 'Granos', 'disponible', 'Proveedor Central'),
    ('Quinoa', 'Quinoa orgánica', 4000, 8, 'Granos', 'disponible', 'Proveedor Central'),
    ('Avena', 'Avena en hojuelas', 1500, 15, 'Granos', 'disponible', 'Proveedor Central'),
    ('Lentejas', 'Lentejas secas', 2000, 12, 'Granos', 'disponible', 'Proveedor Central'),
    ('Porotos', 'Porotos secos', 1800, 10, 'Granos', 'disponible', 'Proveedor Central'),
    ('Garbanzos', 'Garbanzos secos', 2200, 8, 'Granos', 'disponible', 'Proveedor Central'),
    ('Trigo', 'Trigo para moler', 1000, 15, 'Granos', 'disponible', 'Proveedor Central'),
    ('Cebada', 'Cebada perlada', 1600, 10, 'Granos', 'disponible', 'Proveedor Central'),
    ('Maíz', 'Maíz en grano', 1400, 12, 'Granos', 'disponible', 'Proveedor Central'),
    
    # Lácteos
    ('Leche 1L', 'Leche entera', 800, 25, 'Lácteos', 'disponible', 'Proveedor Lácteos'),
    ('Huevos x12', 'Huevos frescos', 1200, 20, 'Lácteos', 'disponible', 'Proveedor Lácteos'),
    ('Queso 200g', 'Queso gouda', 2000, 15, 'Lácteos', 'disponible', 'Proveedor Lácteos'),
    ('Yogurt', 'Yogurt natural', 800, 30, 'Lácteos', 'disponible', 'Proveedor Lácteos'),
    ('Mantequilla', 'Mantequilla 200g', 1500, 20, 'Lácteos', 'disponible', 'Proveedor Lácteos'),
    ('Crema', 'Crema para cocinar', 1200, 15, 'Lácteos', 'disponible', 'Proveedor Lácteos'),
    ('Ricotta', 'Ricotta fresca', 1800, 10, 'Lácteos', 'disponible', 'Proveedor Lácteos'),
    ('Mozzarella', 'Mozzarella fresca', 2500, 12, 'Lácteos', 'disponible', 'Proveedor Lácteos'),
    ('Parmesano', 'Parmesano rallado', 3000, 8, 'Lácteos', 'disponible', 'Proveedor Lácteos'),
    ('Cottage', 'Queso cottage', 1600, 10, 'Lácteos', 'disponible', 'Proveedor Lácteos'),
    
    # Carnes y Embutidos
    ('Jamón 200g', 'Jamón cocido', 1800, 12, 'Carnes', 'disponible', 'Proveedor Carnes'),
    ('Salchichas', 'Salchichas vienesas', 1500, 15, 'Carnes', 'disponible', 'Proveedor Carnes'),
    ('Pollo', 'Pollo entero', 3000, 8, 'Carnes', 'disponible', 'Proveedor Carnes'),
    ('Carne Molida', 'Carne molida fresca', 4000, 6, 'Carnes', 'disponible', 'Proveedor Carnes'),
    ('Pescado', 'Pescado fresco', 3500, 5, 'Carnes', 'disponible', 'Proveedor Carnes'),
    ('Tocino', 'Tocino ahumado', 2500, 8, 'Carnes', 'disponible', 'Proveedor Carnes'),
    ('Chorizo', 'Chorizo parrillero', 2000, 10, 'Carnes', 'disponible', 'Proveedor Carnes'),
    ('Longaniza', 'Longaniza fresca', 2200, 8, 'Carnes', 'disponible', 'Proveedor Carnes'),
    ('Pechuga', 'Pechuga de pollo', 2800, 10, 'Carnes', 'disponible', 'Proveedor Carnes'),
    ('Filete', 'Filete de pescado', 4500, 4, 'Carnes', 'disponible', 'Proveedor Carnes'),
    
    # Panadería
    ('Pan', 'Pan fresco', 500, 30, 'Panadería', 'disponible', 'Proveedor Panadería'),
    ('Pan Integral', 'Pan integral', 800, 20, 'Panadería', 'disponible', 'Proveedor Panadería'),
    ('Croissants', 'Croissants', 600, 15, 'Panadería', 'disponible', 'Proveedor Panadería'),
    ('Galletas', 'Galletas surtidas', 1200, 25, 'Panadería', 'disponible', 'Proveedor Panadería'),
    ('Tortillas', 'Tortillas de harina', 1000, 12, 'Panadería', 'disponible', 'Proveedor Panadería'),
    ('Baguette', 'Baguette francesa', 700, 10, 'Panadería', 'disponible', 'Proveedor Panadería'),
    ('Muffins', 'Muffins caseros', 800, 15, 'Panadería', 'disponible', 'Proveedor Panadería'),
    ('Donas', 'Donas glaseadas', 500, 20, 'Panadería', 'disponible', 'Proveedor Panadería'),
    ('Torta', 'Torta de chocolate', 2500, 3, 'Panadería', 'disponible', 'Proveedor Panadería'),
    ('Empanadas', 'Empanadas de pino', 800, 25, 'Panadería', 'disponible', 'Proveedor Panadería'),
    
    # Bebidas
    ('Café', 'Café molido 500g', 3000, 10, 'Bebidas', 'disponible', 'Proveedor Central'),
    ('Té', 'Té negro 100 bolsas', 2500, 8, 'Bebidas', 'disponible', 'Proveedor Central'),
    ('Jugo', 'Jugo de naranja', 1000, 20, 'Bebidas', 'disponible', 'Proveedor Central'),
    ('Agua', 'Agua mineral', 500, 50, 'Bebidas', 'disponible', 'Proveedor Central'),
    ('Refresco', 'Refresco cola', 800, 30, 'Bebidas', 'disponible', 'Proveedor Central'),
    ('Vino', 'Vino tinto', 2500, 15, 'Bebidas', 'disponible', 'Proveedor Central'),
    ('Cerveza', 'Cerveza nacional', 1200, 25, 'Bebidas', 'disponible', 'Proveedor Central'),
    ('Champagne', 'Champagne', 5000, 5, 'Bebidas', 'disponible', 'Proveedor Central'),
    ('Whisky', 'Whisky escocés', 8000, 3, 'Bebidas', 'disponible', 'Proveedor Central'),
    ('Ron', 'Ron añejo', 6000, 4, 'Bebidas', 'disponible', 'Proveedor Central'),
    
    # Condimentos y Especias
    ('Sal', 'Sal marina', 300, 20, 'Condimentos', 'disponible', 'Proveedor Central'),
    ('Azúcar', 'Azúcar blanca', 1000, 15, 'Condimentos', 'disponible', 'Proveedor Central'),
    ('Aceite', 'Aceite vegetal', 2500, 10, 'Condimentos', 'disponible', 'Proveedor Central'),
    ('Vinagre', 'Vinagre blanco', 800, 25, 'Condimentos', 'disponible', 'Proveedor Central'),
    ('Pimienta', 'Pimienta negra', 1200, 12, 'Condimentos', 'disponible', 'Proveedor Central'),
    ('Orégano', 'Orégano seco', 800, 15, 'Condimentos', 'disponible', 'Proveedor Central'),
    ('Comino', 'Comino molido', 1000, 10, 'Condimentos', 'disponible', 'Proveedor Central'),
    ('Ajo', 'Ajo fresco', 600, 20, 'Condimentos', 'disponible', 'Proveedor Central'),
    ('Cebolla', 'Cebolla deshidratada', 900, 15, 'Condimentos', 'disponible', 'Proveedor Central'),
    ('Laurel', 'Hojas de laurel', 500, 8, 'Condimentos', 'disponible', 'Proveedor Central'),
    
    # Conservas
    ('Atún', 'Atún en lata', 2000, 15, 'Conservas', 'disponible', 'Proveedor Sur'),
    ('Aceitunas', 'Aceitunas verdes', 1500, 20, 'Conservas', 'disponible', 'Proveedor Sur'),
    ('Sardinas', 'Sardinas en lata', 1200, 12, 'Conservas', 'disponible', 'Proveedor Sur'),
    ('Piña en Lata', 'Piña en conserva', 1800, 10, 'Conservas', 'disponible', 'Proveedor Sur'),
    ('Puré de Tomate', 'Puré de tomate en lata', 1000, 15, 'Conservas', 'disponible', 'Proveedor Sur'),
    ('Champiñones', 'Champiñones en lata', 1600, 8, 'Conservas', 'disponible', 'Proveedor Sur'),
    ('Palmitos', 'Palmitos en conserva', 2500, 6, 'Conservas', 'disponible', 'Proveedor Sur'),
    ('Alcachofas', 'Alcachofas en conserva', 2000, 5, 'Conservas', 'disponible', 'Proveedor Sur'),
    ('Espárragos', 'Espárragos en conserva', 2200, 4, 'Conservas', 'disponible', 'Proveedor Sur'),
    ('Salsa de Tomate', 'Salsa de tomate en lata', 1500, 8, 'Conservas', 'disponible', 'Proveedor Sur'),
    
    # Dulces y Snacks
    ('Chocolate', 'Chocolate negro', 2000, 15, 'Dulces', 'disponible', 'Proveedor Central'),
    ('Caramelos', 'Caramelos surtidos', 800, 30, 'Dulces', 'disponible', 'Proveedor Central'),
    ('Chicles', 'Chicles de menta', 500, 40, 'Dulces', 'disponible', 'Proveedor Central'),
    ('Turrón', 'Turrón de almendras', 3000, 8, 'Dulces', 'disponible', 'Proveedor Central'),
    ('Miel', 'Miel natural', 2500, 10, 'Dulces', 'disponible', 'Proveedor Central'),
    ('Mermelada', 'Mermelada de fresa', 1200, 12, 'Dulces', 'disponible', 'Proveedor Central'),
    ('Mantecol', 'Mantecol chileno', 1500, 15, 'Dulces', 'disponible', 'Proveedor Central'),
    ('Alfajores', 'Alfajores surtidos', 1000, 20, 'Dulces', 'disponible', 'Proveedor Central'),
    ('Oreos', 'Galletas Oreo', 1500, 18, 'Dulces', 'disponible', 'Proveedor Central'),
    ('Papas Fritas', 'Papas fritas', 1200, 25, 'Snacks', 'disponible', 'Proveedor Central'),
    
    # Productos de Limpieza
    ('Detergente', 'Detergente líquido', 2000, 15, 'Limpieza', 'disponible', 'Proveedor Central'),
    ('Jabón', 'Jabón de tocador', 800, 30, 'Limpieza', 'disponible', 'Proveedor Central'),
    ('Shampoo', 'Shampoo familiar', 2500, 12, 'Limpieza', 'disponible', 'Proveedor Central'),
    ('Papel', 'Papel higiénico', 1500, 20, 'Limpieza', 'disponible', 'Proveedor Central'),
    ('Toallas', 'Toallas de papel', 1000, 15, 'Limpieza', 'disponible', 'Proveedor Central'),
    ('Limpiavidrios', 'Limpiavidrios', 1200, 10, 'Limpieza', 'disponible', 'Proveedor Central'),
    ('Desinfectante', 'Desinfectante', 1800, 8, 'Limpieza', 'disponible', 'Proveedor Central'),
    ('Escoba', 'Escoba de paja', 2500, 5, 'Limpieza', 'disponible', 'Proveedor Central'),
    ('Trapo', 'Trapo de cocina', 500, 20, 'Limpieza', 'disponible', 'Proveedor Central'),
    ('Esponja', 'Esponja de cocina', 300, 25, 'Limpieza', 'disponible', 'Proveedor Central'),
    
    # Productos de Higiene
    ('Cepillo', 'Cepillo de dientes', 800, 20, 'Higiene', 'disponible', 'Proveedor Central'),
    ('Pasta', 'Pasta dental', 1200, 15, 'Higiene', 'disponible', 'Proveedor Central'),
    ('Hilo', 'Hilo dental', 600, 25, 'Higiene', 'disponible', 'Proveedor Central'),
    ('Desodorante', 'Desodorante', 1500, 12, 'Higiene', 'disponible', 'Proveedor Central'),
    ('Crema', 'Crema hidratante', 2000, 10, 'Higiene', 'disponible', 'Proveedor Central'),
    ('Protector', 'Protector solar', 3000, 8, 'Higiene', 'disponible', 'Proveedor Central'),
    ('Cotonitos', 'Cotonitos', 500, 30, 'Higiene', 'disponible', 'Proveedor Central'),
    ('Toallas', 'Toallas higiénicas', 2500, 15, 'Higiene', 'disponible', 'Proveedor Central'),
    ('Pañales', 'Pañales bebé', 4000, 10, 'Higiene', 'disponible', 'Proveedor Central'),
    ('Toallitas', 'Toallitas húmedas', 1800, 12, 'Higiene', 'disponible', 'Proveedor Central'),
]

def crear_productos_bazar():
    """Crea productos típicos del bazar chileno"""
    print("Creando productos del bazar chileno...")
    
    productos_creados = 0
    for nombre, descripcion, precio, stock, categoria, estado, proveedor in PRODUCTOS_BAZAR_CHILE:
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
            productos_creados += 1
            print(f"Producto creado: {nombre} - ${precio}")
        else:
            print(f"Producto {nombre} ya existe")
    
    print(f"Total productos creados: {productos_creados}")

def crear_ventas_historicas():
    """Crea ventas históricas distribuidas en diferentes meses"""
    print("Creando ventas históricas...")
    
    vendedores = Usuario.objects.filter(username__startswith='vendedor')[:10]
    clientes = Clientes.objects.all()
    productos = Productos.objects.all()
    
    # Crear ventas para los últimos 6 meses
    fecha_inicio = datetime.now() - timedelta(days=180)
    
    ventas_creadas = 0
    for i in range(200):
        # Fecha aleatoria en los últimos 6 meses
        dias_aleatorios = random.randint(0, 180)
        fecha_venta = fecha_inicio + timedelta(days=dias_aleatorios)
        
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
        
        ventas_creadas += 1
        if ventas_creadas % 50 == 0:
            print(f"Ventas creadas: {ventas_creadas}")
    
    print(f"Total ventas creadas: {ventas_creadas}")

def verificar_dashboard():
    """Verifica el dashboard y estadísticas"""
    print("Verificando dashboard y estadísticas...")
    
    from apps.ventas_app.models import Venta
    from apps.djangoVer.models import Productos, Clientes
    
    # Estadísticas generales
    total_ventas = Venta.objects.count()
    total_productos = Productos.objects.count()
    total_clientes = Clientes.objects.count()
    
    # Ventas del día
    hoy = datetime.now().date()
    ventas_hoy = Venta.objects.filter(fecha_venta__date=hoy).count()
    
    # Ventas de la semana
    semana_pasada = datetime.now().date() - timedelta(days=7)
    ventas_semana = Venta.objects.filter(fecha_venta__date__gte=semana_pasada).count()
    
    # Ventas del mes
    mes_pasado = datetime.now().date() - timedelta(days=30)
    ventas_mes = Venta.objects.filter(fecha_venta__date__gte=mes_pasado).count()
    
    # Productos con stock bajo
    productos_stock_bajo = Productos.objects.filter(stock__lt=10).count()
    
    # Productos sin stock
    productos_sin_stock = Productos.objects.filter(stock=0).count()
    
    print(f"=== ESTADÍSTICAS DEL DASHBOARD ===")
    print(f"Total de ventas: {total_ventas}")
    print(f"Total de productos: {total_productos}")
    print(f"Total de clientes: {total_clientes}")
    print(f"Ventas hoy: {ventas_hoy}")
    print(f"Ventas esta semana: {ventas_semana}")
    print(f"Ventas este mes: {ventas_mes}")
    print(f"Productos con stock bajo: {productos_stock_bajo}")
    print(f"Productos sin stock: {productos_sin_stock}")
    
    # Ventas por mes
    print(f"\n=== VENTAS POR MES ===")
    for i in range(6):
        mes = datetime.now().date() - timedelta(days=30*i)
        mes_inicio = mes.replace(day=1)
        if i == 0:
            mes_fin = datetime.now().date()
        else:
            mes_fin = (mes_inicio + timedelta(days=32)).replace(day=1) - timedelta(days=1)
        
        ventas_mes_actual = Venta.objects.filter(
            fecha_venta__date__gte=mes_inicio,
            fecha_venta__date__lte=mes_fin
        ).count()
        
        print(f"{mes_inicio.strftime('%B %Y')}: {ventas_mes_actual} ventas")

def main():
    """Función principal"""
    print("=== CREANDO DATOS MASIVOS DEL BAZAR CHILENO ===")
    print()
    
    try:
        # Crear productos del bazar
        crear_productos_bazar()
        print()
        
        # Crear ventas históricas
        crear_ventas_historicas()
        print()
        
        # Verificar dashboard
        verificar_dashboard()
        print()
        
        print("=== DATOS MASIVOS CREADOS EXITOSAMENTE ===")
        print("Se han creado 100 productos típicos del bazar chileno")
        print("Se han creado 200 ventas distribuidas en los últimos 6 meses")
        print("El dashboard está actualizado con todas las estadísticas")
        
    except Exception as e:
        print(f"Error al crear datos masivos: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()
