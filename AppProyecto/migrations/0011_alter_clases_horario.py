# Generated by Django 4.0.5 on 2022-07-24 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto', '0010_remove_clases_duracion_clases_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clases',
            name='horario',
            field=models.TimeField(max_length=30, null=True),
        ),
    ]