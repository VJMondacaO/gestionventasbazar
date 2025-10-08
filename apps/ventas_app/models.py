from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.utils import timezone
from decimal import Decimal

User = get_user_model()


class Venta(models.Model):
    """
    Modelo para registrar las ventas del bazar según normativa chilena
    """
    TIPO_DOCUMENTO_CHOICES = [
        ('boleta', 'Boleta de Venta'),
        ('factura', 'Factura'),
    ]
    
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    
    numero_venta = models.CharField(max_length=20, unique=True, verbose_name="Número de Venta")
    fecha_venta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Venta")
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ventas', verbose_name="Vendedor")
    cliente = models.ForeignKey('djangoVer.Clientes', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cliente")
    
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO_CHOICES, default='boleta', verbose_name="Tipo de Documento")
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente', verbose_name="Estado")
    
    # Campos específicos para Chile
    rut_cliente = models.CharField(max_length=12, blank=True, null=True, verbose_name="RUT Cliente")
    direccion_cliente = models.CharField(max_length=200, blank=True, null=True, verbose_name="Dirección Cliente")
    comuna_cliente = models.CharField(max_length=50, blank=True, null=True, verbose_name="Comuna Cliente")
    
    # Totales según normativa chilena
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)], verbose_name="Subtotal")
    iva = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)], verbose_name="IVA (19%)")
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)], verbose_name="Total")
    
    # Campos adicionales para Chile
    forma_pago = models.CharField(max_length=20, default='efectivo', verbose_name="Forma de Pago")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones")
    
    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ['-fecha_venta']
    
    def __str__(self):
        return f"Venta {self.numero_venta} - {self.fecha_venta.strftime('%d/%m/%Y %H:%M')}"
    
    def calcular_totales(self):
        """Calcula automáticamente subtotal, IVA y total según normativa chilena"""
        items = self.items.all()
        self.subtotal = sum(item.subtotal for item in items)
        # IVA 19% según normativa chilena
        self.iva = self.subtotal * Decimal('0.19')
        self.total = self.subtotal + self.iva
        self.save()
    
    def generar_numero_venta(self):
        """Genera un número único para la venta"""
        from datetime import datetime
        fecha = datetime.now()
        return f"V{fecha.strftime('%Y%m%d')}{self.id or 1:04d}"


class ItemVenta(models.Model):
    """
    Modelo para los items de cada venta
    """
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='items', verbose_name="Venta")
    producto = models.ForeignKey('djangoVer.Productos', on_delete=models.CASCADE, verbose_name="Producto")
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name="Cantidad")
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="Precio Unitario")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="Subtotal")
    
    class Meta:
        verbose_name = "Item de Venta"
        verbose_name_plural = "Items de Venta"
    
    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"
    
    def save(self, *args, **kwargs):
        """Calcula automáticamente el subtotal"""
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)


class ResumenDiario(models.Model):
    """
    Modelo para generar resúmenes diarios de ventas
    """
    fecha = models.DateField(unique=True, verbose_name="Fecha")
    total_ventas = models.IntegerField(default=0, verbose_name="Total de Ventas")
    total_boletas = models.IntegerField(default=0, verbose_name="Total de Boletas")
    total_facturas = models.IntegerField(default=0, verbose_name="Total de Facturas")
    subtotal_dia = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Subtotal del Día")
    iva_dia = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="IVA del Día")
    total_dia = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Total del Día")
    
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    
    class Meta:
        verbose_name = "Resumen Diario"
        verbose_name_plural = "Resúmenes Diarios"
        ordering = ['-fecha']
    
    def __str__(self):
        return f"Resumen {self.fecha.strftime('%d/%m/%Y')}"
    
    @classmethod
    def generar_resumen_dia(cls, fecha):
        """Genera o actualiza el resumen del día"""
        from django.db.models import Count, Sum
        
        ventas_dia = Venta.objects.filter(fecha_venta__date=fecha, estado='completada')
        
        resumen, created = cls.objects.get_or_create(fecha=fecha)
        resumen.total_ventas = ventas_dia.count()
        resumen.total_boletas = ventas_dia.filter(tipo_documento='boleta').count()
        resumen.total_facturas = ventas_dia.filter(tipo_documento='factura').count()
        
        if ventas_dia.exists():
            resumen.subtotal_dia = ventas_dia.aggregate(Sum('subtotal'))['subtotal__sum'] or 0
            resumen.iva_dia = ventas_dia.aggregate(Sum('iva'))['iva__sum'] or 0
            resumen.total_dia = ventas_dia.aggregate(Sum('total'))['total__sum'] or 0
        else:
            resumen.subtotal_dia = 0
            resumen.iva_dia = 0
            resumen.total_dia = 0
        
        resumen.save()
        return resumen


class ControlDia(models.Model):
    """
    Modelo para controlar el estado del día de ventas
    """
    fecha = models.DateField(unique=True)
    estado = models.CharField(max_length=20, choices=[
        ('abierto', 'Abierto'),
        ('cerrado', 'Cerrado'),
    ], default='abierto')
    fecha_apertura = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    usuario_apertura = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='dias_apertura')
    usuario_cierre = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='dias_cierre')
    observaciones = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Control de Día"
        verbose_name_plural = "Controles de Día"
        ordering = ['-fecha']
    
    def __str__(self):
        return f"{self.fecha.strftime('%d/%m/%Y')} - {self.get_estado_display()}"
    
    @classmethod
    def obtener_estado_dia(cls, fecha):
        """
        Obtiene el estado del día, creando el registro si no existe
        """
        control, created = cls.objects.get_or_create(
            fecha=fecha,
            defaults={'estado': 'abierto'}
        )
        return control
    
    def cerrar_dia(self, usuario, observaciones=''):
        """
        Cierra el día de ventas
        """
        self.estado = 'cerrado'
        self.fecha_cierre = timezone.now()
        self.usuario_cierre = usuario
        self.observaciones = observaciones
        self.save()
    
    def abrir_dia(self, usuario):
        """
        Abre el día de ventas
        """
        self.estado = 'abierto'
        self.fecha_apertura = timezone.now()
        self.usuario_apertura = usuario
        self.fecha_cierre = None
        self.usuario_cierre = None
        self.observaciones = ''
        self.save()
