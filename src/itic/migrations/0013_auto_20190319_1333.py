# Generated by Django 2.1.7 on 2019-03-19 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itic', '0012_archivos_timestamp'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Archivos',
            new_name='Archivo',
        ),
        migrations.RenameModel(
            old_name='Procesos',
            new_name='Proceso',
        ),
    ]