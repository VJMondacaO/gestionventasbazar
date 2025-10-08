from django import forms
from django.core.exceptions import ValidationError
from .models import Venta, ItemVenta
from apps.djangoVer.models import Productos, Clientes


class VentaForm(forms.ModelForm):
    """
    Formulario para crear/editar ventas adaptado para Chile
    """
    FORMA_PAGO_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('transferencia', 'Transferencia'),
        ('tarjeta_debito', 'Tarjeta Débito'),
        ('tarjeta_credito', 'Tarjeta Crédito'),
        ('cheque', 'Cheque'),
    ]
    
    forma_pago = forms.ChoiceField(
        choices=FORMA_PAGO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial='efectivo'
    )
    
    class Meta:
        model = Venta
        fields = ['cliente', 'tipo_documento', 'rut_cliente', 'direccion_cliente', 'comuna_cliente', 'forma_pago', 'observaciones']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control', 'onchange': 'cargarDatosCliente()'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-control', 'onchange': 'toggleFacturaFields()'}),
            'rut_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12.345.678-9'}),
            'direccion_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección del cliente'}),
            'comuna_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comuna del cliente'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Clientes.objects.all()
        self.fields['cliente'].empty_label = "Cliente General"
        self.fields['rut_cliente'].label = "RUT Cliente"
        self.fields['direccion_cliente'].label = "Dirección Cliente"
        self.fields['comuna_cliente'].label = "Comuna Cliente"
        self.fields['forma_pago'].label = "Forma de Pago"


class ItemVentaForm(forms.ModelForm):
    """
    Formulario para agregar items a una venta con cálculo automático
    """
    class Meta:
        model = ItemVenta
        fields = ['producto', 'cantidad', 'precio_unitario']
        widgets = {
            'producto': forms.Select(attrs={
                'class': 'form-control', 
                'onchange': 'actualizarPrecio()',
                'id': 'id_producto'
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control', 
                'min': '1', 
                'onchange': 'calcularSubtotal()',
                'oninput': 'calcularSubtotal()',
                'id': 'id_cantidad'
            }),
            'precio_unitario': forms.NumberInput(attrs={
                'class': 'form-control', 
                'step': '0.01', 
                'onchange': 'calcularSubtotal()',
                'oninput': 'calcularSubtotal()',
                'id': 'id_precio_unitario'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto'].queryset = Productos.objects.filter(stock__gt=0)
        self.fields['producto'].empty_label = "Seleccionar producto"
        self.fields['producto'].label = "Producto"
        self.fields['cantidad'].label = "Cantidad"
        self.fields['precio_unitario'].label = "Precio Unitario"
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        producto = self.cleaned_data.get('producto')
        
        if producto and cantidad:
            if cantidad > producto.stock:
                raise ValidationError(f'No hay suficiente stock. Disponible: {producto.stock}')
        
        return cantidad
    
    def clean_precio_unitario(self):
        precio = self.cleaned_data.get('precio_unitario')
        if precio and precio <= 0:
            raise ValidationError('El precio debe ser mayor a 0')
        return precio


class BuscarVentaForm(forms.Form):
    """
    Formulario para buscar ventas
    """
    TIPO_BUSQUEDA_CHOICES = [
        ('numero', 'Número de Venta'),
        ('fecha', 'Fecha'),
        ('cliente', 'Cliente'),
        ('vendedor', 'Vendedor'),
    ]
    
    tipo_busqueda = forms.ChoiceField(
        choices=TIPO_BUSQUEDA_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    termino = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese término de búsqueda'})
    )
    fecha_desde = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    fecha_hasta = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )


class ResumenDiarioForm(forms.Form):
    """
    Formulario para generar resúmenes diarios
    """
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha and fecha > forms.utils.today():
            raise ValidationError('No se puede generar un resumen para una fecha futura')
        return fecha
