from django.contrib import admin
from .models import User , Blog



class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'std_num', 'password', 'first_name', 'last_name', 'email']


admin.site.register(User,UserAdmin)
admin.site.register(Blog)