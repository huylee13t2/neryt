# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170712_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tag',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
