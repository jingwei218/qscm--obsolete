# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-06 13:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horizon', '0028_auto_20170130_0827'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSheetSetting',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=255)),
                ('data_sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horizon.DataSheet')),
            ],
        ),
        migrations.AlterModelOptions(
            name='schemesetting',
            options={},
        ),
        migrations.AlterModelOptions(
            name='uom',
            options={'ordering': ['pid']},
        ),
        migrations.AddField(
            model_name='setting',
            name='level',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datasheetsetting',
            name='setting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horizon.Setting'),
        ),
    ]