# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 22:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0031_auto_20160121_0046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pair',
            options={'ordering': ['-first_week', 'number']},
        ),
        migrations.RemoveField(
            model_name='pair',
            name='time',
        ),
    ]
