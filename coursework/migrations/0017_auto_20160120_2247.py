# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0016_remove_pair_weekday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='pair',
            name='time',
            field=models.TimeField(default='8:30'),
        ),
        migrations.AddField(
            model_name='pair',
            name='weekday',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coursework.Weekday'),
        ),
    ]