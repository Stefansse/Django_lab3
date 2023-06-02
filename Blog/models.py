from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class BlogUser(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    blocked_users = models.ManyToManyField(User, related_name="blocked_users", blank=True)

    def __str__(self):
        return self.name + " " + self.last_name


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    files = models.FileField(null=True, blank=True)
    date_of_created = models.DateTimeField()
    date_of_last_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content_of_comment = models.CharField(max_length=50)
    date_commented = models.DateTimeField()
    commented_by = models.ForeignKey(BlogUser, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content_of_comment
