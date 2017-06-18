# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horizon', '0071_horizonuser_company'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='setting',
            options={'ordering': ['pid']},
        ),
        migrations.AddField(
            model_name='schemesetting',
            name='locked',
            field=models.BooleanField(default=False),
        ),
    ]
