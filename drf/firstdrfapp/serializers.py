from rest_framework import serializers
from .models import Post,CustomUser
from django.db import transaction
from rest_framework.renderers import JSONRenderer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email','username']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    print("Data Came Up")
    class Meta:
        model = Post
        fields = ['url','title','content','author']
        extra_kwargs = {
            'url': {'view_name': 'post-detail','lookup_field':'pk'},
            'author': {'view_name': 'custom_user-detail','lookup_field':'pk'}
        }

    

