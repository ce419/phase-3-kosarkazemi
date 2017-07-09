from django.db import models
from datetime import datetime
from author import models as author_models


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    blog_owner = models.ForeignKey(author_models.Blog)
    title = models.CharField(max_length=40)
    sum = models.CharField(max_length=150)
    text = models.CharField(max_length=1000)
    datetime = models.DateTimeField()


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post_owner = models.ForeignKey(Post)
    name = models.CharField(max_length=150)
    text = models.CharField(max_length=1000)
    datetime = models.DateTimeField()



