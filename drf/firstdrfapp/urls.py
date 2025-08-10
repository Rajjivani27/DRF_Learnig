from django.urls import path
from .views import *

urlpatterns = [
    path('post-list/',PostListView.as_view(),name='post-list-view'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail-view'),
]