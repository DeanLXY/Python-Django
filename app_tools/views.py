# encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .forms import AddForm

def index(request):
    if request.method == 'POST':
        form = AddForm(request.POST) # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        form = AddForm()
        return render(request,'index.html',{'form':form})
