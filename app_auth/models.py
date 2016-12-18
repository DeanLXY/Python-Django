# -*- coding: utf-8 -*-
from django.db import models
import hashlib
#自己的后台数据库表.account
class Account(models.Model):
    username = models.CharField(u"用户名",blank=True,max_length=32)
    password = models.CharField(u"密码",blank=True,max_length=50)
    check_password = models.CharField(u'确认密码',null=True,max_length=50)
    domain = models.CharField(u"可操作域名",blank=True,max_length=256,help_text='填写多个域名，以,号分隔')
    is_active = models.IntegerField(u"is_active",blank=True,default=False)
    is_superuser = models.BooleanField(u"is_superuser",blank=True,default=True)
    is_staff = models.BooleanField(u"is_staff",blank=True,default=True)
    last_login  = models.DateTimeField(u"上次登录时间",blank=True,null=True)
    date_joined  = models.DateTimeField(u"用户创建的日期",auto_now_add=True,blank=True,null=True)

    phone = models.CharField(u"电话",max_length=50)
    mail = models.CharField(u"邮箱",max_length=50)


    def check_password(self,password):
        if self.password == password:
            return True
        else:
            return False

    def __unicode__(self):
        return self.username
