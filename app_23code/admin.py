from django.contrib import admin
from .models import CodeCategory
# Register your models here.

class CodeCategoryAdmin(admin.ModelAdmin):
    list_display = ('app_title','app_desc','upload_time','app_category')
    search_fields = ('app_title', 'app_category',)
    list_filter = ('app_category','upload_time',)


admin.site.register(CodeCategory,CodeCategoryAdmin)
