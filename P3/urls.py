from django.conf.urls import url
from django.contrib import admin
from author.views import *
from blog.views import *

##TODO sending serverside files

urlpatterns = (
    #author
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_page),
    url(r'^auth/register/', register_page),
    url(r'^auth/login/$', login_page),
    url(r'^auth/logout/$', logout_page),
    url(r'^auth/blog_id/$', blog_id_get),

    #blog
    url(r'^blog/(\d)/posts/$', get_posts),
    url(r'^blog/(\d)/post/$', post),
    url(r'^blog/(\d)/comments/$', get_comments),
    url(r'^blog/(\d)/comment/$', comment),

)





