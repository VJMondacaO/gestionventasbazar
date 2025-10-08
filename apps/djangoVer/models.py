from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, choices=[
        ('disponible', 'Disponible'),
        ('agotado', 'Agotado'),
        ('descontinuado', 'Descontinuado')
    ])
    observaciones = models.TextField(blank=True, null=True)
    proveedor = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Clientes(models.Model):
    """
    Modelo de clientes adaptado para Chile
    """
    TIPO_CLIENTE_CHOICES = [
        ('consumidor_final', 'Consumidor Final'),
        ('contribuyente', 'Contribuyente'),
        ('empresa', 'Empresa'),
    ]
    
    TIPO_PERSONA_CHOICES = [
        ('natural', 'Persona Natural'),
        ('juridica', 'Persona Jurídica'),
    ]
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre/Razón Social")
    rut = models.CharField(max_length=12, unique=True, verbose_name="RUT")
    email = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    direccion = models.CharField(max_length=200, verbose_name="Dirección")
    comuna = models.CharField(max_length=50, default='Santiago', verbose_name="Comuna")
    region = models.CharField(max_length=50, default="Metropolitana", verbose_name="Región")
    fecha_registro = models.DateField(auto_now_add=True, verbose_name="Fecha de Registro")
    
    tipo_cliente = models.CharField(max_length=20, choices=TIPO_CLIENTE_CHOICES, default='consumidor_final', verbose_name="Tipo de Cliente")
    tipo_persona = models.CharField(max_length=20, choices=TIPO_PERSONA_CHOICES, default='natural', verbose_name="Tipo de Persona")
    
    # Campos adicionales para Chile
    giro = models.CharField(max_length=100, blank=True, null=True, verbose_name="Giro")
    contacto = models.CharField(max_length=100, blank=True, null=True, verbose_name="Persona de Contacto")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones")
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre} - {self.rut}"