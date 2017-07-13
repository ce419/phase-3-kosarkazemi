from django.conf.urls import url
from django.contrib import admin

from author.views import main_page
from blog import views
from author.views import logout_page
from author import views
from django.contrib.auth.views import login



urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_page),
    url(r'^register/', views.register.as_view()),
    url(r'^login/$', login),
    url(r'^logout/$', logout_page), )
    # url(r'^posts/', blog.views.posts.as_view()),)


# urlpatterns = patterns('',(r'^$', main_page),(r'^user/(\w+)/$', user_page),(r'^login/$', 'django.contrib.auth.views.login'),)




