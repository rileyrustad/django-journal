# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_auto_20161031_0531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Morning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grateful1', models.CharField(max_length=100, verbose_name='I am grateful for...')),
                ('grateful2', models.CharField(max_length=100, verbose_name='I am grateful for...')),
                ('grateful3', models.CharField(max_length=100, verbose_name='I am grateful for...')),
                ('great1', models.CharField(max_length=100, verbose_name='What would make today great?')),
                ('great2', models.CharField(max_length=100, verbose_name='What would make today great?')),
                ('great3', models.CharField(max_length=100, verbose_name='What would make today great?')),
                ('affirm1', models.CharField(max_length=100, verbose_name='Daily Affirmations, I am...')),
                ('affirm2', models.CharField(max_length=100, verbose_name='Daily Affirmations, I am...')),
            ],
        ),
        migrations.RemoveField(
            model_name='entryresponse',
            name='entry',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='entry',
        ),
        migrations.RemoveField(
            model_name='goalresponse',
            name='goal',
        ),
        migrations.RemoveField(
            model_name='goalresponse',
            name='response',
        ),
        migrations.RemoveField(
            model_name='question',
            name='entry',
        ),
        migrations.RemoveField(
            model_name='questionresponse',
            name='question',
        ),
        migrations.RemoveField(
            model_name='questionresponse',
            name='response',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
        migrations.DeleteModel(
            name='EntryResponse',
        ),
        migrations.DeleteModel(
            name='Goal',
        ),
        migrations.DeleteModel(
            name='GoalResponse',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='QuestionResponse',
        ),
    ]
