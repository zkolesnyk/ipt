# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0017_auto_20160120_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='lecturer',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
