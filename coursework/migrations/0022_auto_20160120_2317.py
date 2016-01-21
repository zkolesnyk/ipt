# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0021_auto_20160120_2307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lecturer',
            options={'ordering': ['fullname']},
        ),
        migrations.RemoveField(
            model_name='subject',
            name='lecturer',
        ),
        migrations.AddField(
            model_name='lecturer',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='coursework.Subject'),
        ),
    ]
