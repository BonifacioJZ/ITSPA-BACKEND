# Generated by Django 2.1.7 on 2019-03-19 13:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('itic', '0011_procesos_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivos',
            name='timestamp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
