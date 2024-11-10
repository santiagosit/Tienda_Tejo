# Generated by Django 5.1.1 on 2024-10-02 02:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_inventario', '0001_initial'),
        ('app_ventas', '0005_producto_alter_ventadetalle_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventadetalle',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventario.producto'),
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
