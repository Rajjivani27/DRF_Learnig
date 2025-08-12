from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users',PostCreateAPI,basename='users')

urlpatterns = [
    path('post-list/',PostListView.as_view(),name='post-list-view'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail-view'),
] + router.urls