from django.urls import path,include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('register_user/',UserCreateAPI.as_view(),name="user-register"),
    path('post_list/',PostListAPI.as_view(),name="post-list"),
    path('post_list/<pk>/',PostListAPI.as_view(),name="post-retrive"),
    path('api/token/',LoginAPI.as_view(),name="token-obtain-api"),
    path('api/token/refresh/',RefreshTokenAPI.as_view(),name="refresh-token-api")
]