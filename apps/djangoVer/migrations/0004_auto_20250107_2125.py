# Generated manually to handle model changes

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoVer', '0003_auto_20251006_2223'),
    ]

    operations = [
        # Rename ID_Cliente to id
        migrations.RenameField(
            model_name='clientes',
            old_name='ID_Cliente',
            new_name='id',
        ),
        # Rename other fields to match new model
        migrations.RenameField(
            model_name='clientes',
            old_name='Nombre_Cliente',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='Correo',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='Telefono',
            new_name='telefono',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='Direccion',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='Ciudad',
            new_name='comuna',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='Pais',
            new_name='region',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='Fecha_Registro',
            new_name='fecha_registro',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='Tipo_Cliente',
            new_name='tipo_cliente',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='Preferencias',
            new_name='observaciones',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='Fecha_Nacimiento',
            new_name='fecha_nacimiento',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='Genero',
            new_name='genero',
        ),
        
        # Add new fields
        migrations.AddField(
            model_name='clientes',
            name='rut',
            field=models.CharField(max_length=12, unique=True, default='12.345.678-9'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientes',
            name='tipo_persona',
            field=models.CharField(max_length=20, choices=[('natural', 'Persona Natural'), ('juridica', 'Persona Jurídica')], default='natural'),
        ),
        migrations.AddField(
            model_name='clientes',
            name='giro',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clientes',
            name='contacto',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        
        # Update field types and constraints
        migrations.AlterField(
            model_name='clientes',
            name='comuna',
            field=models.CharField(max_length=50, default='Santiago'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='region',
            field=models.CharField(max_length=50, default='Metropolitana'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='tipo_cliente',
            field=models.CharField(max_length=20, choices=[('consumidor_final', 'Consumidor Final'), ('contribuyente', 'Contribuyente'), ('empresa', 'Empresa')], default='consumidor_final'),
        ),
    ]
