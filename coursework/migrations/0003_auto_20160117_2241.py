# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0002_auto_20160117_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
    ]
