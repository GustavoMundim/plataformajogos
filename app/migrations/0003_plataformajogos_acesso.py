# Generated by Django 5.0.4 on 2024-04-18 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_plataformajogos_data_criacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plataformajogos',
            name='acesso',
            field=models.IntegerField(default=0),
        ),
    ]