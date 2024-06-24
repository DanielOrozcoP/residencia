# Generated by Django 4.2.13 on 2024-06-23 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuarto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carnet_identidad', models.CharField(max_length=11, unique=True, verbose_name='Carnet de Identidad')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('facultad', models.CharField(max_length=100, verbose_name='Facultad')),
                ('carrera', models.CharField(max_length=100, verbose_name='Carrera')),
                ('ano_academico', models.IntegerField(null=True, verbose_name='Año academico')),
                ('eliminado', models.BooleanField(default=False, verbose_name='Eliminado')),
                ('cuarto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cuarto.cuarto', verbose_name='cuarto')),
            ],
        ),
    ]
