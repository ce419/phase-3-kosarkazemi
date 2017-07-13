from django.conf.urls import url
from django.contrib import admin
from blog import views
from author import views


urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^register/', views.register.as_view()),
    url(r'^login/$', 'django.contrib.auth.views.login')
    # url(r'^posts/', blog.views.posts.as_view()),
)

# urlpatterns = patterns('',(r'^$', main_page),(r'^user/(\w+)/$', user_page),(r'^login/$', 'django.contrib.auth.views.login'),)




