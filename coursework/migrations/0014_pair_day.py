# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0013_auto_20160120_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='pair',
            name='day',
            field=models.IntegerField(default=0),
        ),
    ]