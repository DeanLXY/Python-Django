# coding=utf-8
from django.contrib import admin
from .models import CodeCategory
# Register your models here.

class CodeCategoryAdmin(admin.ModelAdmin):
    list_display = ('preview','app_title','app_desc','update_time','app_category')
    search_fields = ('app_title', 'app_category',)
    list_filter = ('app_category',)
    list_per_page = 20
    # list_select_related = ('app_category',)

    def preview(self,obj):
        return '<img src="/static/images/%s" height="288" width="167" />' %(obj.img_convery)

    preview.allow_tags = True

    preview.short_description = u"效果图"


admin.site.register(CodeCategory,CodeCategoryAdmin)
