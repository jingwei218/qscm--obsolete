# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horizon', '0108_remove_datasheet_datasheet_elements'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasheet',
            name='datasheet_elements',
            field=models.ManyToManyField(to='horizon.DataSheetElement'),
        ),
    ]
