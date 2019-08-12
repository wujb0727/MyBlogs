"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
                  path('', views.home, name='home'),  # 主页路径
                  path('admin/', admin.site.urls),
                  path('ckeditor', include('ckeditor_uploader.urls')),  # 配置上传url
                  path('blog/', include('blog.urls')),  # 博客app路径
                  path('comment/', include('comment.urls')),  # 评论app路径
                  path('likes/', include('likes.urls')),  # 点赞app路径
                  path('login/', views.login, name='login'),  # 登录
                  path('login_form_model/', views.login_for_model, name='login_for_model'),  # 登录
                  path('register/', views.register, name='register'),  # 注册
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 设置ckeditor的上传
