"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home, delete_view, like_view, profile, editprofile, hashtag_view, handler404
from loginpage.views import accounts, login_view, signup_view, logout_view
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('', accounts, name='accounts'),
    path('accounts/', accounts, name='accounts'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('signup/', signup_view, name='signup_view'),
    path('home/delete', delete_view, name='delete_view'),
    path('home/hashtag', hashtag_view, name='hashtag_view'),
    path('profilepage/delete', delete_view, name='delete_view'),
    path('like/<int:pk>', like_view, name='like_post'),
    path('profilepage/', profile, name='profile'),
    path('<int:pk>/editprofile/', editprofile.as_view(), name='editprofile'),
    url(r'^$', handler404),

] 
handler404 = 'home.views.handler404'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
