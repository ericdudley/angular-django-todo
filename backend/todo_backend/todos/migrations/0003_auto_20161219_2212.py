# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20161219_2203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-time_created']},
        ),
        migrations.AlterField(
            model_name='todo',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
