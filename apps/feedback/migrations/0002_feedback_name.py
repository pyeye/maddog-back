# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-19 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='name',
            field=models.CharField(default='test', max_length=255, verbose_name='Имя'),
            preserve_default=False,
        ),
    ]