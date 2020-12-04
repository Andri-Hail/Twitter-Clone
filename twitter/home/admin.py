from django.contrib import admin
from home.models import Tweet, Profile, Reply
# Register your models here.

admin.site.register(Tweet)
admin.site.register(Profile)
admin.site.register(Reply)