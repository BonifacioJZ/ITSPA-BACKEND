# Generated by Django 2.1.7 on 2019-04-02 13:30

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('itic', '0022_auto_20190402_0206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proceso',
            name='notas',
        ),
        migrations.AlterField(
            model_name='proceso',
            name='descripcion',
            field=tinymce.models.HTMLField(),
        ),
    ]
