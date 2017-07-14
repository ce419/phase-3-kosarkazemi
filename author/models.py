from django.db import models
from django.contrib.auth.models import User


class BlogUser(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    blog_id = models.IntegerField(default=0)
    token = models.CharField(max_length=20, blank=True, null=True, default=None)

    ###  TODO



class Blog(models.Model):
    owner = models.ForeignKey(BlogUser, blank=True, null=True)
