# 🏪 Sistema de Gestión de Ventas - Bazar Chile

## 📋 Contexto y Objetivo

**Contexto:** Un pequeño bazar en Chile necesita modernizar su gestión de ventas, que actualmente es manual. Se requiere una solución para el control digital de transacciones, emisión de comprobantes y generación de resúmenes diarios, cumpliendo con la normativa fiscal chilena.

**Objetivo:** Desarrollar una aplicación web para registrar ventas, calcular automáticamente el IVA (19%) y el total, generar vistas previas de boletas/facturas y producir informes de ventas diarios para el jefe de ventas, adaptado a la normativa chilena.

## 🚀 Características Principales

### ✅ Módulo de Autenticación y Roles
- **Sistema de login** con validación de credenciales
- **Dos roles de usuario**: Vendedor y Jefe de Ventas
- **Redirección automática** según el rol del usuario
- **Interfaces diferenciadas** por nivel de acceso

### ✅ Sistema de Gestión de Ventas
- **Registro de ventas** con múltiples productos
- **Cálculo automático** de IVA (19%) según normativa chilena
- **Gestión de stock** automática al realizar ventas
- **Tipos de documento**: Boletas de Venta y Facturas
- **Estados de venta**: Pendiente, Completada, Cancelada
- **Campos específicos para Chile**: RUT, dirección, comuna
- **Formas de pago**: Efectivo, transferencia, tarjetas, cheque

### ✅ Dashboard y Reportes
- **Dashboard principal** con estadísticas en tiempo real
- **Resúmenes diarios** de ventas
- **Listado de ventas** con filtros avanzados
- **Productos más vendidos**
- **Estadísticas de ingresos** por día y mes

### ✅ Gestión de Productos y Clientes
- **Catálogo de productos** con precios en pesos chilenos (CLP)
- **Base de datos de clientes** con RUT y datos chilenos
- **Control de inventario** automático
- **Tipos de cliente**: Consumidor Final, Contribuyente, Empresa
- **Datos geográficos**: Comuna, región

## 🏗️ Arquitectura del Sistema

```
gestionVentasBazar/
├── apps/
│   ├── auth_app/                    # 🔐 Autenticación y roles
│   ├── ventas_app/                  # 💰 Sistema de ventas
│   └── djangoVer/      # 📦 Productos y clientes
├── templates/                       # 📄 Plantillas HTML
├── static/                         # 🎨 Archivos estáticos
└── manage.py                       # 🚀 Archivo principal
```

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 5.0
- **Base de datos**: MySQL
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Autenticación**: Django Auth con modelo personalizado
- **Formularios**: Django Forms con validación
- **Normativa**: Adaptado a normativa fiscal chilena
- **Moneda**: Pesos Chilenos (CLP)
- **IVA**: 19% según normativa chilena

## 📦 Instalación y Configuración

### 1. Clonar el repositorio
```bash
cd gestionVentasBazar
```

### 2. Instalar dependencias
```bash
pip install django pymysql
```

### 3. Configurar base de datos
Editar `gestionVentasBazar/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bazar_db',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña'
    }
}
```

### 4. Aplicar migraciones
```bash
python manage.py migrate
```

### 5. Inicializar sistema
```bash
python init_system.py
```

### 6. Ejecutar servidor
```bash
python manage.py runserver
```

## 👥 Usuarios de Prueba

| Rol | Usuario | Contraseña | Acceso |
|-----|---------|------------|-------|
| Vendedor | vendedor1 | vendedor123 | Sistema de ventas |
| Jefe de Ventas | jefe1 | jefe123 | Dashboard completo |
| Administrador | admin | admin123 | Panel administrativo |

## 🎯 Funcionalidades por Rol

### 👤 Vendedor
- ✅ Crear nuevas ventas
- ✅ Agregar productos a ventas
- ✅ Calcular totales automáticamente
- ✅ Finalizar ventas
- ✅ Ver historial de ventas propias

### 👑 Jefe de Ventas
- ✅ Todas las funciones del vendedor
- ✅ Ver todas las ventas del sistema
- ✅ Generar resúmenes diarios
- ✅ Acceso a estadísticas completas
- ✅ Gestión de usuarios

## 📊 Características del Sistema

### 💰 Gestión de Ventas
- **Número de venta único** generado automáticamente
- **Cálculo automático de IVA** (19%)
- **Control de stock** en tiempo real
- **Múltiples productos** por venta
- **Estados de venta** configurables

### 📈 Dashboard y Reportes
- **Estadísticas en tiempo real**
- **Ventas del día y mes**
- **Productos más vendidos**
- **Resúmenes diarios automáticos**
- **Filtros avanzados** de búsqueda

### 🛡️ Seguridad
- **Autenticación requerida** para todas las funciones
- **Roles y permisos** diferenciados
- **Validación de formularios**
- **Protección CSRF**

## 🚀 Uso del Sistema

### 1. Iniciar Sesión
- Acceder a `http://localhost:8000/auth/login/`
- Ingresar credenciales de usuario
- El sistema redirigirá automáticamente según el rol

### 2. Crear una Venta
1. Hacer clic en "Nueva Venta"
2. Seleccionar cliente y tipo de documento
3. Agregar productos con cantidades
4. El sistema calculará automáticamente totales
5. Finalizar la venta

### 3. Ver Reportes
- **Dashboard**: Estadísticas generales
- **Listar Ventas**: Historial completo con filtros
- **Resumen Diario**: Reportes por fecha específica

## 🔧 Configuración Avanzada

### Personalizar IVA
Editar en `apps/ventas_app/models.py`:
```python
self.iva = self.subtotal * Decimal('0.19')  # Cambiar porcentaje
```

### Agregar Nuevos Estados de Venta
Modificar `ESTADO_CHOICES` en el modelo `Venta`:
```python
ESTADO_CHOICES = [
    ('pendiente', 'Pendiente'),
    ('completada', 'Completada'),
    ('cancelada', 'Cancelada'),
    ('nuevo_estado', 'Nuevo Estado'),
]
```

## 📱 Responsive Design

El sistema está optimizado para:
- 💻 **Desktop**: Experiencia completa
- 📱 **Tablet**: Navegación adaptada
- 📱 **Mobile**: Interfaz móvil optimizada

## 🐛 Solución de Problemas

### Error de Migraciones
```bash
python manage.py migrate --fake-initial
```

### Error de Base de Datos
Verificar configuración en `settings.py` y credenciales de MySQL.

### Error de Permisos
Ejecutar `python init_system.py` para crear usuarios de prueba.

## 📞 Soporte

Para soporte técnico o consultas:
- 📧 Email: soporte@bazar.com
- 📱 Teléfono: +56 9 1234 5678
- 🌐 Web: www.bazar.com/soporte

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

---

**Desarrollado con ❤️ para la modernización del comercio local**
