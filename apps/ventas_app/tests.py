from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from decimal import Decimal
from .models import Venta, ItemVenta, ResumenDiario
from apps.djangoVer.models import Productos, Clientes

User = get_user_model()


class VentasTestCase(TestCase):
    def setUp(self):
        # Crear usuario vendedor
        self.vendedor = User.objects.create_user(
            username='vendedor1',
            password='testpass123',
            rol='vendedor'
        )
        
        # Crear cliente
        self.cliente = Clientes.objects.create(
            nombre='Cliente Test',
            email='cliente@test.com',
            telefono='123456789'
        )
        
        # Crear producto
        self.producto = Productos.objects.create(
            nombre='Producto Test',
            precio=Decimal('1000.00'),
            stock=10
        )
    
    def test_crear_venta(self):
        """Test para crear una nueva venta"""
        venta = Venta.objects.create(
            numero_venta='V202501070001',
            vendedor=self.vendedor,
            cliente=self.cliente,
            tipo_documento='boleta'
        )
        
        self.assertEqual(venta.vendedor, self.vendedor)
        self.assertEqual(venta.cliente, self.cliente)
        self.assertEqual(venta.tipo_documento, 'boleta')
        self.assertEqual(venta.estado, 'pendiente')
    
    def test_agregar_item_venta(self):
        """Test para agregar items a una venta"""
        venta = Venta.objects.create(
            numero_venta='V202501070002',
            vendedor=self.vendedor,
            cliente=self.cliente
        )
        
        item = ItemVenta.objects.create(
            venta=venta,
            producto=self.producto,
            cantidad=2,
            precio_unitario=Decimal('1000.00')
        )
        
        self.assertEqual(item.subtotal, Decimal('2000.00'))
        self.assertEqual(venta.items.count(), 1)
    
    def test_calcular_totales_venta(self):
        """Test para calcular totales de una venta"""
        venta = Venta.objects.create(
            numero_venta='V202501070003',
            vendedor=self.vendedor,
            cliente=self.cliente
        )
        
        # Agregar items
        ItemVenta.objects.create(
            venta=venta,
            producto=self.producto,
            cantidad=2,
            precio_unitario=Decimal('1000.00')
        )
        
        venta.calcular_totales()
        
        self.assertEqual(venta.subtotal, Decimal('2000.00'))
        self.assertEqual(venta.iva, Decimal('380.00'))  # 19% de 2000
        self.assertEqual(venta.total, Decimal('2380.00'))
    
    def test_generar_resumen_diario(self):
        """Test para generar resumen diario"""
        from datetime import date
        
        # Crear venta completada
        venta = Venta.objects.create(
            numero_venta='V202501070004',
            vendedor=self.vendedor,
            cliente=self.cliente,
            estado='completada',
            subtotal=Decimal('1000.00'),
            iva=Decimal('190.00'),
            total=Decimal('1190.00')
        )
        
        # Generar resumen
        resumen = ResumenDiario.generar_resumen_dia(date.today())
        
        self.assertEqual(resumen.total_ventas, 1)
        self.assertEqual(resumen.total_dia, Decimal('1190.00'))
    
    def test_actualizar_stock_producto(self):
        """Test para verificar que se actualiza el stock al vender"""
        stock_inicial = self.producto.stock
        
        venta = Venta.objects.create(
            numero_venta='V202501070005',
            vendedor=self.vendedor,
            cliente=self.cliente
        )
        
        ItemVenta.objects.create(
            venta=venta,
            producto=self.producto,
            cantidad=3,
            precio_unitario=Decimal('1000.00')
        )
        
        # El stock debe haberse reducido
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.stock, stock_inicial - 3)
