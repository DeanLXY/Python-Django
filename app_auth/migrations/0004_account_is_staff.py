# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0003_auto_20161217_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_staff',
            field=models.IntegerField(blank=True, null=True, verbose_name='is_staff'),
        ),
    ]
