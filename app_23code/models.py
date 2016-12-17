# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.

class CodeCategory(models.Model):

    img_convery = models.CharField(u'效果图',max_length=1000)
    app_title = models.CharField(u'名称',max_length=20,null=True)
    upload_author= models.CharField(u'上传',max_length=60,null=True)
    update_time = models.DateTimeField(u'更新时间',auto_now_add=True,null=True)
    category_txt_href = models.CharField(u'链接',max_length=200)
    app_category = models.CharField(u'分类',max_length=20,editable=False)
    app_desc = UEditorField(u'描述',height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')

