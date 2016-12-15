# -*- encoding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    sum = int(a) + int(b)
    return HttpResponse(str(sum))


def add2(request,a,b):
    return HttpResponse(str(int(a) + int(b)))
