# Generated by Django 5.1.4 on 2025-01-23 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_alter_produto_data_de_criacao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="data_de_criacao",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
