# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horizon', '0064_auto_20170601_1317'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricecondition',
            options={'ordering': ['pid']},
        ),
        migrations.AddField(
            model_name='pricesheet',
            name='number_of_fields',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
