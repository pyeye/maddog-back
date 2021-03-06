# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-18 19:03
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Созданно')),
                ('contact', models.CharField(blank=True, max_length=255, null=True, verbose_name='Контакт')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, verbose_name='Экстра')),
            ],
            options={
                'verbose_name_plural': 'Обратная связь',
                'verbose_name': 'Обратная связь',
            },
        ),
    ]
