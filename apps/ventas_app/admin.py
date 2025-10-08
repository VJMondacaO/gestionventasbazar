from django.contrib import admin
from .models import Venta, ItemVenta, ResumenDiario


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('numero_venta', 'fecha_venta', 'vendedor', 'cliente', 'tipo_documento', 'estado', 'total')
    list_filter = ('estado', 'tipo_documento', 'fecha_venta', 'vendedor')
    search_fields = ('numero_venta', 'vendedor__username', 'cliente__nombre')
    readonly_fields = ('numero_venta', 'fecha_venta', 'subtotal', 'iva', 'total')
    ordering = ('-fecha_venta',)
    
    fieldsets = (
        ('Información General', {
            'fields': ('numero_venta', 'fecha_venta', 'vendedor', 'cliente')
        }),
        ('Documento', {
            'fields': ('tipo_documento', 'estado')
        }),
        ('Totales', {
            'fields': ('subtotal', 'iva', 'total'),
            'classes': ('collapse',)
        }),
        ('Observaciones', {
            'fields': ('observaciones',),
            'classes': ('collapse',)
        }),
    )


@admin.register(ItemVenta)
class ItemVentaAdmin(admin.ModelAdmin):
    list_display = ('venta', 'producto', 'cantidad', 'precio_unitario', 'subtotal')
    list_filter = ('venta__fecha_venta', 'producto')
    search_fields = ('venta__numero_venta', 'producto__nombre')
    readonly_fields = ('subtotal',)


@admin.register(ResumenDiario)
class ResumenDiarioAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'total_ventas', 'total_boletas', 'total_facturas', 'total_dia')
    list_filter = ('fecha',)
    search_fields = ('fecha',)
    readonly_fields = ('fecha_creacion',)
    ordering = ('-fecha',)
    
    fieldsets = (
        ('Fecha', {
            'fields': ('fecha', 'fecha_creacion')
        }),
        ('Cantidades', {
            'fields': ('total_ventas', 'total_boletas', 'total_facturas')
        }),
        ('Totales', {
            'fields': ('subtotal_dia', 'iva_dia', 'total_dia')
        }),
    )
