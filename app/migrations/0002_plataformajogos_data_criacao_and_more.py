# Generated by Django 5.0.4 on 2024-04-18 15:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plataformajogos',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='plataformajogos',
            name='preco_jogo',
            field=models.FloatField(),
        ),
    ]
