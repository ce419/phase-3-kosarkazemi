from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    std_num = models.IntegerField()
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    user_owner = models.ForeignKey(User)
