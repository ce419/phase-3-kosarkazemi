from django.db import models
from django.utils import timezone
from author import models as author_models


class Post(models.Model):
    blog = models.ForeignKey(author_models.Blog)
    title = models.CharField(max_length=40)
    sum = models.CharField(max_length=150)
    text = models.CharField(max_length=1000)
    datetime = models.DateTimeField(default=timezone.now)

    def get_map(self):
        ret = {
            'id': self.id,
            'title': self.title,
            'summery': self.sum,
            'datetime': self.datetime,
            'text': self.text
        }


class Comment(models.Model):
    post = models.ForeignKey(Post)
    name = models.CharField(max_length=150)
    text = models.CharField(max_length=1000)
    datetime = models.DateTimeField(default=timezone.now)



