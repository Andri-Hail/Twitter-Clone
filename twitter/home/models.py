from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # on_delete=models.DO_NOTHING is so that when tweet gets deleted the author doesn't
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='post')
    # hashtags = models.ManyToManyField(Hashtag, related_name='post') # Moved this relation from Tweet to Hashtag


    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

class Hashtag(models.Model):
    
    word = models.CharField(max_length=200)
    tweets = models.ManyToManyField(Tweet, related_name='tag')

    def __str__(self):
        return "#" + self.word