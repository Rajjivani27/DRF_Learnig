from rest_framework import serializers 
from rest_framework.exceptions import ValidationError
from .models import *
from mongoengine.errors import NotUniqueError

class CustomUserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only = True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField()
    password2 = serializers.CharField(write_only=True,required=True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Both passwords are not matching")
        return data


    def create(self, validated_data):
        try:
            validated_data.pop('password2')
            password = validated_data.pop('password')
            user = CustomUser(**validated_data)
            user.set_password(password)
            print(user.email)
            print(user.email)
            user.save()
            print(user)
            return user
        except NotUniqueError:
            return ("A user with either same email or username already exist. Please enter the unique value")
        

class PostSerializer(serializers.Serializer):
    id = serializers.CharField(read_only = True)
    title = serializers.CharField()
    content = serializers.CharField()
    author = serializers.CharField(source='author.id',read_only=True)