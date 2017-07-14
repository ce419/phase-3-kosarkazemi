from django.db import models
from django.utils import timezone
from author import models as author_models

#request.META['X-Token']

class Post(models.Model):
    blog = models.ForeignKey(author_models.Blog)
    title = models.CharField(max_length=40)
    sum = models.CharField(max_length=150)
    text = models.CharField(max_length=1000)
    datetime = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    name = models.CharField(max_length=150)
    text = models.CharField(max_length=1000)
    datetime = models.DateTimeField(default=timezone.now)



