"""Hello_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import index
from app_calc.views import add
from app_calc.views import add2
from app_temp.views import index as temp_index
from app_23code.views import create as code_create
from app_23code.views import list as code_list
from app_blog2.views import index as blog_index
from app_blog2.views import add as blog_add

urlpatterns = [
    url(r'^index/',blog_index),
    url(r'^create/$',code_create),
    url(r'^codelist/$',code_list),
    url(r'^add/$', blog_add),
    # url(r'^index/(\w+)/$', temp_index),
    url(r'^add/(\d+)/(\d+)/$',add2),
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
]
