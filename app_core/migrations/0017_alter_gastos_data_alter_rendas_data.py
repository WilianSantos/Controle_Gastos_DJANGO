# Generated by Django 4.2 on 2023-04-22 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0016_alter_gastos_data_alter_rendas_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastos',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 4, 22, 13, 26, 35, 9991)),
        ),
        migrations.AlterField(
            model_name='rendas',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 4, 22, 13, 26, 35, 9991)),
        ),
    ]