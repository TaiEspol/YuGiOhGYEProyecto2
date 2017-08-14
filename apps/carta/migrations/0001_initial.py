# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carta',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('producto', models.ManyToManyField(to='producto.Producto')),
            ],
            options={
                'db_table': 'carta',
            },
        ),
    ]
