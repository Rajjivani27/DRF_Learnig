from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'posts',PostViewSet,basename='post')

urlpatterns = [
    path('post-list/',PostListView.as_view(),name='post-list-view'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail-view'),
    path('user_detail/<int:pk>/',CustomUserDetail.as_view(),name="custom_user-detail"),
    #path('post_detail/<int:pk>/',PostDetail.as_view(),name="post-detail")
] + router.urls