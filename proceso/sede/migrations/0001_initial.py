# Generated by Django 4.2.13 on 2024-06-23 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15, unique=True, verbose_name='codigo')),
                ('direccion', models.CharField(max_length=250, verbose_name='direccion')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
            ],
        ),
    ]