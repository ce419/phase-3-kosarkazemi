from django.conf.urls import url
from django.contrib import admin
from author.views import *
from blog.views import *
from django.contrib.auth.views import login



urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_page),
    url(r'^register/', register_page),
    url(r'^login/$', login),
    url(r'^logout/$', logout_page),
)





