# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_finished', models.DateTimeField(null=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('finished', models.BooleanField(default=False)),
            ],
        ),
    ]
