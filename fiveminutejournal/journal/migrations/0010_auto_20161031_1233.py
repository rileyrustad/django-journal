# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 19:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0009_auto_20161031_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='goal',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 7, 19, 33, 40, 689739, tzinfo=utc)),
        ),
    ]