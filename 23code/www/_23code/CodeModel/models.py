# -*- encoding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
#CREATE TABLE if not exists list_info(id INT NOT NULL primary key AUTO_INCREMENT,img_convery varchar(1000),app_title varchar(60),upload_time varchar(60),app_desc varchar(200),category_txt_href varchar(200),app_category varchar(20))

# 类名 是表名 属性是列
class list_info(models.Model):
    img_convery = models.CharField(max_length=1000)
    app_title = models.CharField(max_length=60)
    upload_time = models.CharField(max_length=60)
    app_desc = models.CharField(max_length=200)
    category_txt_href = models.CharField(max_length=200)
    app_category = models.CharField(max_length=20)


