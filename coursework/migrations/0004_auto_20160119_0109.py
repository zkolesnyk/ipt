# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0003_auto_20160117_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lecturer', models.CharField(max_length=40)),
                ('lecture_hall', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
