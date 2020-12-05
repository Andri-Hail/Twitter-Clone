from django.shortcuts import render, redirect, get_object_or_404
from home.models import Tweet, Profile, Reply
from home.models import Tweet, Hashtag
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
import re
from django.views import generic

from django.views.generic.edit import UpdateView

# Create your views here.

# def homepage(request):
#     return render(request, "homepage.html", {})

    

def like_view(request, pk):
    tweet = get_object_or_404(Tweet, id=request.POST.get('post_id'))

    if tweet.likes.filter(id=request.user.id).exists():
        tweet.likes.remove(request.user)
    else:
        tweet.likes.add(request.user)  
    return redirect(request.META['HTTP_REFERER'])


class editprofile(generic.UpdateView):
    model = Profile
    template_name = 'editprofile.html'
    fields = ['bio', 'profile_pic']
    success_url = '/profilepage'




def profile(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/')
   
    username = request.user
    tweets = Tweet.objects.all()
    my_tweets = set()
    liked_tweets = set()
    tweet_count = 0
    for tweet in tweets:
        if tweet.likes.filter(id=request.user.id).exists():
            liked_tweets.add(tweet)

    for tweet in tweets:
        if tweet.author == username:
            tweet_count += 1
            my_tweets.add(tweet)
    if tweet_count == 1:
        append = 'tweet'
    else:
        append = 'tweets'

    return render(request, 'profilepage.html', {'tweets' : tweets, 'liked_tweets' : liked_tweets, 'my_tweets' : my_tweets, 'username' : username, 'tweet_count' : tweet_count, 'append' : append })


def home(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/')
    #Insert data into DB if post:
    if 'submit_tweet' in request.POST:
        if request.method == 'POST' and request.POST['body'] !="":
            text = request.POST['body']
            #create tweet:
            tweet = Tweet.objects.create (
                body = text,
                author = request.user
            )
    elif request.method == 'POST' and request.POST['body'] !="":
        parent = Tweet.objects.get(id=request.POST.get('reply', ""))
        reply = Reply.objects.create (
            og_tweet = parent,
            body = request.POST['body'],
            name = request.user
            )

    username = request.user
    tweets = Tweet.objects.all()
    liked_tweets = set()
    hashtaglist = set()
    for tweet in tweets:
        if tweet.likes.filter(id=request.user.id).exists():
            liked_tweets.add(tweet)
            tweet.liked = True
         #Parse out hashtags and add them to Model, related to Tweet
        hashtags = re.findall(r"#(\w+)", tweet.body)
        for hashtag in hashtags:
            hashtaglist.add(hashtag)
            try:
                hashtag_obj = Hashtag.objects.get(word=hashtag)
            except Hashtag.DoesNotExist as exc:
                hashtag_obj = Hashtag.objects.create(word=hashtag)
            hashtag_obj.tweets.add(tweet)
            
    hashtags = Hashtag.objects.all()

    return render(request, 'homepage.html', {'tweets' : tweets, 'liked_tweets' : liked_tweets, 'username' : username, 'hashtaglist' : hashtaglist, 'hashtags' : hashtags})


def hashtag_view(request):
        
    tag = request.GET['tag']
    tag_obj = Hashtag.objects.get(word=tag)
    taggedtweets = tag_obj.tweets.all()
    hashtags = Hashtag.objects.all()

    username = request.user
    tweets = Tweet.objects.all()
    liked_tweets = set()
    hashtaglist = set()

    for tweet in taggedtweets:
        if tweet.likes.filter(id=request.user.id).exists():
            tweet.liked = True



    for tweet in tweets:
        if tweet.likes.filter(id=request.user.id).exists():
            liked_tweets.add(tweet)
            tweet.liked = True
         #Parse out hashtags and add them to Model, related to Tweet
        hashtags = re.findall(r"#(\w+)", tweet.body)
        for hashtag in hashtags:
            hashtaglist.add(hashtag)
            try:
                hashtag_obj = Hashtag.objects.get(word=hashtag)
            except Hashtag.DoesNotExist as exc:
                hashtag_obj = Hashtag.objects.create(word=hashtag)
            hashtag_obj.tweets.add(tweet)
            
    hashtags = Hashtag.objects.all()
    return render(request, 'homepage.html', {'tag' : tag, 'hashtags':hashtags, 'hashtaglist':hashtaglist,'username' : username, 'taggedtweets' : taggedtweets, 'tweets' : tweets})

def delete_view(request):
    tweet = Tweet.objects.get(id=request.GET['id'])
    if tweet.author == request.user:
        tweet.delete()
    return redirect(request.META['HTTP_REFERER'])
