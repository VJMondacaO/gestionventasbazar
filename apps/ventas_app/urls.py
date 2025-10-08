from django.urls import path
from . import views

app_name = 'ventas_app'

urlpatterns = [
    # Dashboard y resumen
    path('', views.dashboard_ventas, name='dashboard_ventas'),
    path('reportes/', views.reportes_diarios, name='reportes_diarios'),
    path('resumen/', views.resumen_diario, name='resumen_diario'),
    path('resumen/<int:resumen_id>/', views.detalle_resumen, name='detalle_resumen'),
    
    # Gestión de ventas
    path('nueva/', views.nueva_venta, name='nueva_venta'),
    path('venta/<int:venta_id>/items/', views.agregar_items, name='agregar_items'),
    path('venta/<int:venta_id>/', views.detalle_venta, name='detalle_venta'),
    path('venta/<int:venta_id>/previa/', views.vista_previa_comprobante, name='vista_previa_comprobante'),
    path('venta/<int:venta_id>/finalizar/', views.finalizar_venta, name='finalizar_venta'),
    path('venta/<int:venta_id>/boleta/', views.generar_boleta, name='generar_boleta'),
    path('listar/', views.listar_ventas, name='listar_ventas'),
    
    # Gestión de items
    path('item/<int:item_id>/eliminar/', views.eliminar_item, name='eliminar_item'),
    
    # Control de Día (Solo Jefe de Ventas)
    path('control-dia/', views.control_dia, name='control_dia'),
    path('cerrar-dia/', views.cerrar_dia, name='cerrar_dia'),
    path('abrir-dia/', views.abrir_dia, name='abrir_dia'),
    
    # APIs
    path('api/producto/<int:producto_id>/precio/', views.obtener_precio_producto, name='obtener_precio_producto'),
    path('api/clientes/', views.obtener_clientes, name='obtener_clientes'),
    path('api/estadisticas/', views.obtener_estadisticas_dashboard_ventas, name='estadisticas_dashboard_ventas'),
]
