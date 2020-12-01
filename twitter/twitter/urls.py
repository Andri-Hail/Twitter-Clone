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
from home.views import homepage
from loginpage.views import accounts, login_view, signup_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage, name='homepage'),
    path('', accounts, name='accounts'),
    path('accounts/', accounts, name='accounts'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('signup/', signup_view, name='signup_view'),

    # path('', login, name='login'),
    path('', homepage, name='home')
]