# Generated by Django 4.2 on 2023-05-29 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Siete', '0005_prioridad_tarea_usuario_asignado_alter_tarea_usuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prioridad',
            name='orden',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='prioridad',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
    ]
