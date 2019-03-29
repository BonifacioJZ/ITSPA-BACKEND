# Generated by Django 2.1.7 on 2019-03-29 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itic', '0018_remove_archivo_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='archivo_proceso',
            field=models.ManyToManyField(blank=True, null=True, to='itic.Archivo', verbose_name='archivos'),
        ),
    ]
