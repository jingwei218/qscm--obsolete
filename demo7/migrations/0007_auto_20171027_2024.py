# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo7', '0006_auto_20171025_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='templateelement',
            name='node_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='templateelement',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='templateelement',
            name='html',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='templateelement',
            name='positionX',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='templateelement',
            name='positionY',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='templateelement',
            name='reportTemplate',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='demo7.ReportTemplate'),
        ),
        migrations.AlterField(
            model_name='templateelement',
            name='width',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
