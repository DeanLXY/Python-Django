# -*- encoding:utf-8 -*-

from django.http import HttpResponse

from CodeModel.models import list_info
from django.shortcuts import render
import json
# 数据库操作
def db_list_info(request):
    # 初始化
    response = ""
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list_categories_infos = list_info.objects.all()
    # 输出所有数据
    for app_info in list_categories_infos:
        response += app_info.app_title
        context          = {}
        context['app_title'] = app_info.app_title
        context['upload_time'] = app_info.upload_time
        context['app_desc'] = app_info.app_desc
        context['app_category'] = app_info.app_category
    return render(request, 'category_list.html', context)
