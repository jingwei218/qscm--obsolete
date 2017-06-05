# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horizon', '0063_price_sequence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='sequence',
        ),
        migrations.AddField(
            model_name='pricecondition',
            name='common_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
