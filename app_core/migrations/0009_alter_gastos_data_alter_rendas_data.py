# Generated by Django 4.2 on 2023-04-21 21:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0008_alter_gastos_data_alter_rendas_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastos',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 18, 34, 57, 825281)),
        ),
        migrations.AlterField(
            model_name='rendas',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 18, 34, 57, 825281)),
        ),
    ]
