# Generated by Django 4.2.5 on 2023-10-03 22:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_fotografia_data_fotografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateField(default=datetime.datetime.now, editable=False),
        ),
    ]
