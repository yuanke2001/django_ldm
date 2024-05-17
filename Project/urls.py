"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from DiffusionModel import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    #登录
    path('login/', views.login),
    #注册
    path('register/', views.register),
    #生成界面
    path('gen/', views.gen),
    path('user_list/', views.show_data),
    # path('',views.user_logout())
    path('user_logout/', views.user_logout),
    # path('user_logout/', views.user_logout),
    #后台用户界面
    # # path('user_list/', views.user_list),
    # path('logout/', views.my_logout, name='logout'),
    # path('profile/', views.profile, name='profile'),
]
