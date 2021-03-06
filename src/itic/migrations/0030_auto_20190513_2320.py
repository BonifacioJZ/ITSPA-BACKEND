# Generated by Django 2.2.1 on 2019-05-13 23:20

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('itic', '0029_new_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='actualizado',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='body',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='descripcion',
            field=tinymce.models.HTMLField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='tags',
            field=models.ManyToManyField(to='itic.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='new',
            name='timestamp',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
