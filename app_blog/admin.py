from django.contrib import admin

# Register your models here.
# from django.contrib import admin
from .models import Article
# from app_blog2.models import Person


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update_time',)


# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('full_name',)

admin.site.register(Article)
# admin.site.register(Person, PersonAdmin)
