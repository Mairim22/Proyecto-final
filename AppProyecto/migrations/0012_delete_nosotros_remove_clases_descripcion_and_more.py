# Generated by Django 4.0.5 on 2022-07-24 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto', '0011_alter_clases_horario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Nosotros',
        ),
        migrations.RemoveField(
            model_name='clases',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='clases',
            name='horario',
            field=models.TimeField(max_length=30),
        ),
    ]
