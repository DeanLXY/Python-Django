# coding: utf-8

# DJANGO IMPORTS
from django.contrib import admin

# PROJECT IMPORTS
from grappelli.tests.models import Category, Entry,MyInlineModel

site = admin.AdminSite(name="Admin Site")


class CategoryOptions(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("name",)


class EntryOptions(admin.ModelAdmin):
    list_display = ("id", "title", "category", "user",)
    list_display_links = ("title",)

    def get_queryset(self, request):
        qs = super(EntryOptions, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


class ModelOptions(admin.ModelAdmin):
    fieldsets = (
        ('', {
            'fields': ('title', 'subtitle', 'slug', 'pub_date', 'status',),
        }),
        ('Flags', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('flag_front', 'flag_sticky', 'flag_allow_comments', 'flag_comments_closed',),
        }),
        ('Tags', {
            'classes': ('grp-collapse grp-open',),
            'fields' : ('tags',),
        }),
    )

class StackedItemInline(admin.StackedInline):
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class TabularItemInline(admin.TabularInline):
    classes = ('grp-collapse grp-open',)

site.register(Category, CategoryOptions)
site.register(Entry, EntryOptions)
site.register(MyInlineModel, ModelOptions)
