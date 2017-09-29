# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 01:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horizon', '0100_element_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='horizon.Category'),
        ),
        migrations.AlterField(
            model_name='element',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
