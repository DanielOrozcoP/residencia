# Generated by Django 4.2.13 on 2024-06-23 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dormitorio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuarto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, unique=True, verbose_name='Cuarto')),
                ('capacidad', models.IntegerField(verbose_name='capacidad')),
                ('ocupacion', models.IntegerField(default=0, verbose_name='ocupacion')),
                ('dormitorioID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dormitorio.dormitorio', verbose_name='dormitorio')),
            ],
        ),
    ]
