from django.urls import path
from .views import *

urlpatterns = [
    path('snippets/',snippet_list),
    path('snippets/<int:pk>/',snippets_detail),
]