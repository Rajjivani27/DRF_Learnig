from rest_framework import serializers 
from rest_framework.exceptions import ValidationError,AuthenticationFailed
from .models import *
from mongoengine.errors import NotUniqueError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.tokens import RefreshToken


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
            for key in validated_data:
                print(key)

            validated_data.pop('password2')
            password = validated_data.pop('password')
            user = CustomUser(**validated_data)
            user.set_password(password)
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

    def create(self, validated_data):
        post = Post(**validated_data)
        post.save()

        return post

class CustomTokenPairObtainSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            user = CustomUser.objects.get(email = email)
        except ObjectDoesNotExist:
            raise AuthenticationFailed("Invalid Credentials")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Invalid Credentials")
        
        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access" : str(refresh.access_token)
        }
    
class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, data):
        refresh_token = data.get('refresh_token')

        refresh = RefreshToken(refresh_token)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }
        