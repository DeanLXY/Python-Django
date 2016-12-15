# coding:utf-8

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import format_html


STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)


# Create your models here.
@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')

    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)
    status = models.CharField(u'状态',max_length=1,null=True,choices=STATUS_CHOICES)
    pub_usr = models.CharField(u'创建人',max_length=20,editable=True,null=True,choices=None)

    def __unicode__(self):# 在Python3中用 __str__ 代替 __unicode__
        return self.title

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Person(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=6,null=True)

    def my_property(self):
        return self.first_name + ' ' + self.last_name
    my_property.short_description = "Full name of the person"

    full_name = property(my_property)

    def __str__(self):
        return self.first_name +' * '+self.last_name

    def colored_name(self):
        return format_html(
            '<span style="color: #{};">{} {}</span>',
            self.color_code,
            self.first_name,
            self.last_name,
        )

