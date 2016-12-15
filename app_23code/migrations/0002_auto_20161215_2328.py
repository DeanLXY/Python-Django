# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_23code', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codecategory',
            name='app_category',
            field=models.CharField(max_length=20, verbose_name='\u5206\u7c7b'),
        ),
        migrations.AlterField(
            model_name='codecategory',
            name='app_desc',
            field=models.CharField(max_length=200, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='codecategory',
            name='app_title',
            field=models.CharField(max_length=60, verbose_name='\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='codecategory',
            name='category_txt_href',
            field=models.CharField(max_length=200, verbose_name='\u94fe\u63a5'),
        ),
        migrations.AlterField(
            model_name='codecategory',
            name='img_convery',
            field=models.CharField(max_length=1000, verbose_name='\u6548\u679c\u56fe'),
        ),
        migrations.AlterField(
            model_name='codecategory',
            name='upload_time',
            field=models.CharField(max_length=60, verbose_name='\u4e0a\u4f20\u65f6\u95f4'),
        ),
    ]
