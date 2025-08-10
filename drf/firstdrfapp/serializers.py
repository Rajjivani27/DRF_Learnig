from rest_framework import serializers
from .models import Post,CustomUser
from django.db import transaction

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','content']

    @transaction.atomic
    def create(self,request,**validated_data):
        post = Post(**validated_data)
        

        return post