from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    """
    Modelo de usuario personalizado con roles específicos
    """
    ROLES_CHOICES = [
        ('vendedor', 'Vendedor'),
        ('jefe_ventas', 'Jefe de Ventas'),
    ]
    
    rol = models.CharField(
        max_length=20,
        choices=ROLES_CHOICES,
        default='vendedor',
        help_text='Rol del usuario en el sistema'
    )
    
    def __str__(self):
        return f"{self.username} - {self.get_rol_display()}"
    
    def es_vendedor(self):
        return self.rol == 'vendedor'
    
    def es_jefe_ventas(self):
        return self.rol == 'jefe_ventas'
