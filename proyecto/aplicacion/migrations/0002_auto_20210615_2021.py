# Generated by Django 3.2.4 on 2021-06-16 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=17)),
                ('patente', models.CharField(max_length=17)),
                ('año_de_fabricacion', models.DateField(blank=True, null=True)),
                ('fecha_de_recepcion', models.DateField(blank=True, null=True)),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Trabajador',
        ),
    ]
