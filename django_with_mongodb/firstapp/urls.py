from django.urls import path,include
from .views import *

urlpatterns = [
    path('register_user/',UserCreateAPI.as_view(),name="user-register"),
    path('post_list/',PostListAPI.as_view(),name="post-list"),
    path('post_list/<pk>/',PostListAPI.as_view(),name="post-retrive"),
]