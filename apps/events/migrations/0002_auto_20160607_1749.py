# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-07 17:49
from __future__ import unicode_literals

import datetime
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 7, 17, 49, 2, 73745, tzinfo=utc), verbose_name='Созданно'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='extra',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True, verbose_name='Дополнительно'),
        ),
    ]
