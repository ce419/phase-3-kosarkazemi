from django.contrib import admin
from .models import Post,Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'blog_id']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'post']




admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)

