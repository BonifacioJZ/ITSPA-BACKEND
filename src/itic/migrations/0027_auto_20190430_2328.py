# Generated by Django 2.2 on 2019-04-30 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itic', '0026_auto_20190430_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Noticia',
        ),
    ]
