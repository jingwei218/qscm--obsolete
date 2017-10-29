# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo7', '0007_auto_20171027_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templateelement',
            name='node_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='templateelement',
            name='reportTemplate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='demo7.ReportTemplate'),
        ),
    ]
