# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horizon', '0074_auto_20170623_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='horizonsetting',
            name='hash_pid',
            field=models.CharField(default='0', max_length=255),
        ),
    ]
