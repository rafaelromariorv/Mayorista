# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-06 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='serie',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
