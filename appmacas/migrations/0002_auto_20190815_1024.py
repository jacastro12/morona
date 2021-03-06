# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-08-15 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appmacas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleados',
            name='id_tipoausencias',
        ),
        migrations.AlterField(
            model_name='permisos',
            name='id_empleados',
            field=models.ForeignKey(db_column='id_empleados', on_delete=django.db.models.deletion.DO_NOTHING, to='appmacas.Empleados', verbose_name='Empleado'),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='id_tipoausencias',
            field=models.ForeignKey(db_column='id_tipoausencias', on_delete=django.db.models.deletion.DO_NOTHING, to='appmacas.TipoAusencias', verbose_name='Tipo de Ausencia'),
        ),
    ]
