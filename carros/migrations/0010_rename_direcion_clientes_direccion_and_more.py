# Generated by Django 5.1 on 2024-10-22 06:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0009_alter_auto_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='Direcion',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='No_licencia',
        ),
        migrations.RemoveField(
            model_name='reservaciones',
            name='clientes',
        ),
        migrations.RemoveField(
            model_name='reservaciones',
            name='entradas',
        ),
        migrations.AddField(
            model_name='reservaciones',
            name='cliente',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='carros.clientes'),
        ),
        migrations.AddField(
            model_name='reservaciones',
            name='entrada',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.CharField(default='0000', max_length=8),
        ),
        migrations.AlterField(
            model_name='reservaciones',
            name='matricula',
            field=models.ForeignKey(default='0000', on_delete=django.db.models.deletion.CASCADE, to='carros.auto'),
        ),
        migrations.AlterField(
            model_name='reservaciones',
            name='entrada',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='clientes',
            name='no_licencia',
            field=models.CharField(default='0000', max_length=10),
        ),
    ]
