from django.contrib import admin
from .models import BlogUser , Blog



class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email','blog_id']

    def username(self, obj):
        if obj.user is None:
            return None
        return obj.user.username

    def first_name(self, obj):
        if obj.user is None:
            return None
        return obj.user.first_name

    def last_name(self, obj):
        if obj.user is None:
            return None
        return obj.user.last_name

    def email(self, obj):
        if obj.user is None:
            return None
        return obj.user.email


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner']

    def get_queryset(self, request):
        qs = super(BlogAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            print(request.user)
            for blog in qs.filter(owner__user=request.user):
                print(blog)
            return qs.filter(owner__user=request.user)

admin.site.register(BlogUser,UserAdmin)
admin.site.register(Blog, BlogAdmin)