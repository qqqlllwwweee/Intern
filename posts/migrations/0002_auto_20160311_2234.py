# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-11 22:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 11, 22, 34, 27, 700782)),
        ),
        migrations.AlterField(
            model_name='songs',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 11, 22, 34, 27, 700744)),
        ),
    ]