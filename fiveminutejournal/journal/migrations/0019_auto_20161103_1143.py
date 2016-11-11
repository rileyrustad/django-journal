# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 18:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0018_auto_20161103_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 10, 18, 43, 25, 168883, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='journal',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]