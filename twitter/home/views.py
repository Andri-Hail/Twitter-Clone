from django.shortcuts import render, redirect, get_object_or_404
from home.models import Tweet
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
import re
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

def profile(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/')
    #Insert data into DB if post:
   
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
    if request.method == 'POST':
        text = request.POST['body']

        #create tweet:
        tweet = Tweet.objects.create (
            body = text,
            author = request.user

        )
    username = request.user
    tweets = Tweet.objects.all()
    liked_tweets = set()
    for tweet in tweets:
        if tweet.likes.filter(id=request.user.id).exists():
            liked_tweets.add(tweet)


    return render(request, 'homepage.html', {'tweets' : tweets, 'liked_tweets' : liked_tweets, 'username' : username})


def delete_view(request):
    tweet = Tweet.objects.get(id=request.GET['id'])
    if tweet.author == request.user:
        tweet.delete()
    return redirect(request.META['HTTP_REFERER'])
