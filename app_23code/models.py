from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CodeCategory(models.Model):
    img_convery = models.CharField(max_length=1000)
    app_title = models.CharField(max_length=60)
    upload_time = models.CharField(max_length=60)
    app_desc = models.CharField(max_length=200)
    category_txt_href = models.CharField(max_length=200)
    app_category = models.CharField(max_length=20)
