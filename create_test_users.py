#!/usr/bin/env python
"""
Script para crear usuarios de prueba para el sistema de autenticación
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestionVentasBazar.settings')
django.setup()

from apps.auth_app.models import Usuario

def create_test_users():
    """Crear usuarios de prueba"""
    
    # Crear vendedor
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
        print("✅ Usuario vendedor creado: vendedor1 / vendedor123")
    else:
        print("ℹ️  Usuario vendedor ya existe")
    
    # Crear jefe de ventas
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
        print("✅ Usuario jefe de ventas creado: jefe1 / jefe123")
    else:
        print("ℹ️  Usuario jefe de ventas ya existe")
    
    # Crear superusuario
    admin, created = Usuario.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@bazar.com',
            'first_name': 'Administrador',
            'last_name': 'Sistema',
            'rol': 'jefe_ventas',
            'is_staff': True,
            'is_superuser': True,
            'is_active': True
        }
    )
    if created:
        admin.set_password('admin123')
        admin.save()
        print("✅ Superusuario creado: admin / admin123")
    else:
        print("ℹ️  Superusuario ya existe")

if __name__ == '__main__':
    try:
        create_test_users()
        print("\n🎉 Usuarios de prueba creados exitosamente!")
        print("\nCredenciales de acceso:")
        print("👤 Vendedor: vendedor1 / vendedor123")
        print("👑 Jefe de Ventas: jefe1 / jefe123")
        print("🔧 Administrador: admin / admin123")
    except Exception as e:
        print(f"❌ Error al crear usuarios: {e}")
        sys.exit(1)
