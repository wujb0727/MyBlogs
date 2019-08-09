from django.urls import path
from . import views

urlpatterns = [
    path('update_comment', views.update_commit, name='update_comment'),
]
