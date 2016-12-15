# coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CodeCategory(models.Model):
    img_convery = models.CharField(u'效果图',max_length=1000)
    app_title = models.CharField(u'名称',max_length=20)
    upload_time = models.CharField(u'上传时间',max_length=60)
    app_desc = models.CharField(u'描述',max_length=200)
    category_txt_href = models.CharField(u'链接',max_length=200)
    app_category = models.CharField(u'分类',max_length=20)
