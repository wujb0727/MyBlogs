# encoding: utf-8
# @Author: TiAmo
# @Project: MyBlogs 
# @Time: 2019/8/12 15:14

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),  # 登录
    path('login_form_model/', views.login_for_model, name='login_for_model'),  # 登录
    path('register/', views.register, name='register'),  # 注册
    path('logout/', views.logout, name='logout'),  # 登出
    path('user_info/', views.user_info, name='user_info'),  # 登录
]
