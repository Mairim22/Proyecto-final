# Generated by Django 4.0.5 on 2022-07-25 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto', '0013_clases_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clases',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
    ]
