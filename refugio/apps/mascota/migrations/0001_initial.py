# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-03-05 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=50)),
                ('edad_aproximada', models.IntegerField()),
                ('fecha_recate', models.DateField()),
            ],
        ),
    ]
