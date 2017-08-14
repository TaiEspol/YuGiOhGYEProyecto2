# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 23:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ygoapp', '0001_initial'),
        ('comentario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60)),
                ('fecha', models.DateField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ygoapp.Usuario')),
            ],
            options={
                'db_table': 'tema',
            },
        ),
    ]
