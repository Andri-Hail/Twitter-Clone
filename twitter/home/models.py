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
    liked = models.BooleanField(default=False)


    def total_likes(self):
        return self.likes.count()

class Profile(models.Model):
    user = models.OneToOneField(User,  null=True, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now=True)
    bio = models.TextField(default = "Write your bio here")
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return str(self.user)
    
class Reply(models.Model):
    #Ties the reply to the original tweet. If tweet gets deleted so do replies.
    og_tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="replies")
    name = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)




class Hashtag(models.Model):
    
    word = models.CharField(max_length=200)
    tweets = models.ManyToManyField(Tweet, related_name='tag')

    def __str__(self):
        return "#" + self.word
