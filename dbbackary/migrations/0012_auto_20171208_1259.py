# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-08 12:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbbackary', '0011_auto_20171208_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receitas',
            name='idgood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbbackary.goods'),
        ),
    ]
