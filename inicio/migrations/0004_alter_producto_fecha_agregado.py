# Generated by Django 5.1.3 on 2024-12-30 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_producto_fecha_agregado_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_agregado',
            field=models.DateField(blank=True, null=True),
        ),
    ]
