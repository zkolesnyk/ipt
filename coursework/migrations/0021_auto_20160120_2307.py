# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 21:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0020_auto_20160120_2305'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='lecturer',
            table='lecturer',
        ),
        migrations.AlterModelTable(
            name='pair',
            table='pairs',
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
        migrations.AlterModelTable(
            name='studymaterial',
            table='study materials',
        ),
        migrations.AlterModelTable(
            name='subject',
            table='subject',
        ),
    ]