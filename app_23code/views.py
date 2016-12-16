# -*- encoding:utf-8 -*-
from django.shortcuts import render
from app_23code.models import CodeCategory

# Create your views here.
def create(request):
    # img_convery = models.CharField(max_length=1000)
    # app_title = models.CharField(max_length=60)
    # upload_time = models.CharField(max_length=60)
    # app_desc = models.CharField(max_length=200)
    # category_txt_href = models.CharField(max_length=200)
    # app_category = models.CharField(max_length=20)
    img_convery = request.GET['img_convery']
    app_title = request.GET['app_title']
    upload_time = request.GET['upload_time']
    app_desc = request.GET['app_desc']
    category_txt_href = request.GET['category_txt_href']
    app_category = request.GET['app_category']
    CodeCategory.objects.create(img_convery=img_convery,app_title=app_title,upload_author=upload_time,app_desc=app_desc,category_txt_href=category_txt_href,app_category=app_category)
    return render(request,'spider_create.html',{'app_name':app_title})

def list(request):
    query_set = CodeCategory.objects.all()
    return render(request,'code_list.html',{'code_category_list':[]})
