# Generated by Django 5.0.3 on 2024-03-10 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurante',
            name='preco',
        ),
    ]
