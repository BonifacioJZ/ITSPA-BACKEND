# Generated by Django 2.2 on 2019-04-29 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itspa', '0006_auto_20190429_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='actualizado',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='noticia',
            name='timestamp',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
