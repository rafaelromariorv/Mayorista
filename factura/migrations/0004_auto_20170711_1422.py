# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-11 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0003_factura_iva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='serie',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]