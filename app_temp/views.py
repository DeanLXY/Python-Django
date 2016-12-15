# -*- encoding:utf-8 -*-
from django.shortcuts import render

# Create your views here.

def index1(request):
    return render(request,'index.htm')

def index(request,name):
    #name = '测试用户名'
    return render(request,'index.htm',{'usrname':name})
