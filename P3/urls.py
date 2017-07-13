from django.conf.urls import url
from django.contrib import admin
from author.views import *
from blog.views import *
from django.contrib.auth.views import login



urlpatterns = (
    #author
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_page),
    url(r'^auth/register/', register_page),
    url(r'^auth/login/$', login_page),
    url(r'^lauth/ogout/$', logout_page),
    url(r'^auth/blog_id/$', blog_id_get),

    #blog

)





