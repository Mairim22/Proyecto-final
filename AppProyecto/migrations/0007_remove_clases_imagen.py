# Generated by Django 4.0.5 on 2022-07-22 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto', '0006_clases_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clases',
            name='imagen',
        ),
    ]
