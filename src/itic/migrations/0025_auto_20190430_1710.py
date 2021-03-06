# Generated by Django 2.2 on 2019-04-30 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itic', '0024_auto_20190420_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('actualizado', models.DateField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='nombre',
            new_name='name',
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', tinymce.models.HTMLField(blank=True, max_length=300, null=True)),
                ('body', tinymce.models.HTMLField(blank=True, null=True)),
                ('timestamp', models.DateField(auto_now_add=True, null=True)),
                ('actualizado', models.DateField(auto_now=True, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Autor', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='itic.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Formacion_Academica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('institucion', models.CharField(blank=True, max_length=100, null=True)),
                ('abrebiacion', models.CharField(blank=True, max_length=10, null=True)),
                ('nivel', models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='itic.Nivel')),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='formacion',
            field=models.ManyToManyField(blank=True, to='itic.Formacion_Academica', verbose_name='Formacion Academica'),
        ),
    ]
