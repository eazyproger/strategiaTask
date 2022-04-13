from django.db import models


class Article(models.Model):
    content = models.CharField(max_length=10000)
    comments = models.ManyToManyField('Comment', blank=True)


class Comment(models.Model):
    content = models.CharField(max_length=1000)
    comments = models.ManyToManyField('Comment', blank=True)
    level = models.IntegerField()
