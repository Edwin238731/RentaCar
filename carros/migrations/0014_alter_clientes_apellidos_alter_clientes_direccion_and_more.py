# Generated by Django 5.1.2 on 2024-12-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0013_rename_reservaciones_reservacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='apellidos',
            field=models.CharField(default='0000', max_length=10),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(default='0000', max_length=10),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nombre',
            field=models.CharField(default='0000', max_length=10),
        ),
    ]
