# encoding: utf-8
# @Author: TiAmo
# @Project: MyBlogs 
# @Time: 2019/8/10 9:39

from django.urls import path
from . import views

urlpatterns = [
    path('like_change', views.like_change, name='like_change'),
]
