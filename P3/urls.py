from django.conf.urls import url
from django.contrib import admin
from blog import views
from author import views
from rest_framework.urlpatterns import  format_suffix_patterns

urlpatterns = (
    url(r'^admin/', admin.site.urls),
    # url(r'^posts/', blog.views.posts.as_view()),
    url(r'^register/', views.register.as_view()),
)




