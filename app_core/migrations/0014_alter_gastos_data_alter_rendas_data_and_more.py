# Generated by Django 4.2 on 2023-04-22 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0013_alter_gastos_data_alter_rendas_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastos',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 4, 22, 13, 15, 47, 997070)),
        ),
        migrations.AlterField(
            model_name='rendas',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 22, 13, 15, 47, 997070)),
        ),
        migrations.AlterField(
            model_name='rendas',
            name='renda_principal',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='rendas',
            name='renda_secundaria',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]