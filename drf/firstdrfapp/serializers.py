from rest_framework import serializers
from .models import Post,CustomUser
from django.db import transaction
from rest_framework.renderers import JSONRenderer

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    created_at = serializers.DateTimeField()

    def create(self,validated_data):
        print(validated_data)
        post = Post(**validated_data)
        post.save()
        return post

