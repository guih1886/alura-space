# Generated by Django 4.2.5 on 2023-10-03 22:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_ativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateField(default=datetime.datetime(2023, 10, 3, 19, 41, 20, 949506), editable=False),
        ),
    ]
