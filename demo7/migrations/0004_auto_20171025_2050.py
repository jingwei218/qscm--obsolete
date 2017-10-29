# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo7', '0003_auto_20171024_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node', models.CharField(max_length=100)),
                ('nodeClass', models.CharField(max_length=255)),
                ('positionX', models.FloatField()),
                ('positionY', models.FloatField()),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('reportTemplate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo7.ReportTemplate')),
            ],
        ),
        migrations.RemoveField(
            model_name='printableelement',
            name='reportTemplate',
        ),
        migrations.DeleteModel(
            name='PrintableElement',
        ),
    ]
