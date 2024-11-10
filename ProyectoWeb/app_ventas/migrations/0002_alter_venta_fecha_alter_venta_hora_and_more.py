# Generated by Django 5.1.1 on 2024-10-02 02:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_inventario', '0001_initial'),
        ('app_ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='venta',
            name='hora',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='venta',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventas_ventas', to='app_inventario.producto'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
