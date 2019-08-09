from django.urls import path, re_path, resolvers
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    # name 表示别名
    path('<int:blog_pk>', views.blog_detail, name='blog_detail'),
    # 根据类型分类
    path('type/<int:blog_type_pk>', views.blogs_with_type, name='blogs_with_type'),
    # 根据日期分类
    path('date/<int:year>/<int:month>', views.blogs_with_date, name='blogs_with_date'),
]
