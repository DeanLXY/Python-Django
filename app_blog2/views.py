# encoding:utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import EmailMultiAlternatives


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return render(request,'index.html')

# def add(request):
#     a = request.GET['a']
#     b = request.GET['b']
#     # return HttpResponse('result:'+str(int(a)+ int(b)))
#     return render(request,'index.html',{'result':str(int(a)+ int(b))})



def send_Email_msg(request):
    subject = '来自xxxx的问候'
    text_content = '这是一封重要的邮件.'
    html_content = '<p>这是一封<strong>重要的</strong>邮件.</p>'
    from_email = settings.DEFAULT_FROM_EMAIL
    msg = EmailMultiAlternatives(subject, text_content, from_email, ['774137461@qq.com'])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return HttpResponse(u'succss')
