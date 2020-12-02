from django.shortcuts import render, redirect, get_object_or_404
from home.models import Tweet, Hashtag
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
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
    return redirect('/home/')

    # return HttpResponseRedirect(reverse('tweet', args=[str(pk)]))
def profile(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/')
    #Insert data into DB if post:
   
    username = request.user
    tweets = Tweet.objects.all()
    my_tweets = set()
    liked_tweets = set()
    for tweet in tweets:
        if tweet.likes.filter(id=request.user.id).exists():
            liked_tweets.add(tweet)

    for tweet in tweets:
        if tweet.author == username:
            my_tweets.add(tweet)

    return render(request, 'profilepage.html', {'tweets' : tweets, 'liked_tweets' : liked_tweets, 'my_tweets' : my_tweets, 'username' : username})


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
        
        #Parse out hashtags and add them to Model, related to Tweet
        hashtags = re.findall(r"#(\w+)", text)
        for hashtag in hashtags:
            try:
                hashtag_obj = Hashtag.objects.get(word=hashtag)
            except Hashtag.DoesNotExist as exc:
                hashtag_obj = Hashtag.objects.create(word=hashtag)
            hashtag_obj.tweets.add(tweet)


    username = request.user
    tweets = Tweet.objects.all()
    liked_tweets = set()
    for tweet in tweets:
        if tweet.likes.filter(id=request.user.id).exists():
            liked_tweets.add(tweet)

    hashtags = Hashtag.objects.all()

    return render(request, 'homepage.html', {'tweets' : tweets, 'liked_tweets' : liked_tweets, 'username' : username, 'hashtags' : hashtags})


# Work in progress
def hashtag_view(request):
        
    tag = request.GET['tag']
    tag_obj = Hashtag.objects.get(word=tag)
    tweets = tag_obj.tweets.all()

    return render(request, 'hashtagpage.html', {'tag' : tag, 'tweets' : tweets})

def delete_view(request):
    tweet = Tweet.objects.get(id=request.GET['id'])
    if tweet.author == request.user:
        tweet.delete()
    return redirect('/home/')
