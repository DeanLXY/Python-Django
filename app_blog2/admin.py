from django.contrib import admin,messages

# Register your models here.
from .models import Article, Person

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date', 'update_time','pub_usr','status',)
    field = ('pub_date', 'update_time')
    search_fields = ('title', 'content',)
    list_filter = ('status',)
    empty_value_display = 'None'
    actions = ['make_published','make_ariticle_w']

    # actions_on_top = False
    # actions_on_top = True
    # date_hierarchy = 'pub_date'

    # field = ('status','pub_usr')

    # def status(self, obj):
        # return obj.status

    # status.empty_value_display = '?????'

    def make_published(modeladmin, request, queryset):
        rows_update = queryset.update(status='p')
        if rows_update == 1:
            message_bit = '1 story was'
        else:
            message_bit = '%s story was' % rows_update
        messages.success(request,'%s successfully marked as published.' % message_bit)

    def make_ariticle_w(modeladmin,request,queryset):
        queryset.update(status='w')




    make_published.short_description = "Mark selected stories as published"
    make_ariticle_w.short_description = "Mark selected stories as Withdrawn"

    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)

    # save user info on save article
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


    def formfield_for_choice_field(self, db_field, request, **kwargs):
        # if db_field.name == "status":
        #     kwargs['choices'] = (
        #         ('accepted', 'Accepted'),
        #         ('denied', 'Denied'),
        #     )
        #     if request.user.is_superuser:
        #         kwargs['choices'] += (('ready', 'Ready for deployment'),)

        if db_field.name == 'pub_usr':
            kwargs['choices'] = (
                    ('pub_usr',request.user),
                )

        return super(ArticleAdmin, self).formfield_for_choice_field(db_field, request, **kwargs)



class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name','colored_name')
    list_filter = ('first_name',)

admin.site.register(Article,ArticleAdmin)
admin.site.register(Person,PersonAdmin)
