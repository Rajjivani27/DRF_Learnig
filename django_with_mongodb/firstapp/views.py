from .models import *
from .serializers import PostSerializer,CustomUserSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin

class UserCreateAPI(GenericAPIView,CreateModelMixin):
    serializer_class = CustomUserSerializer
    def post(self,request,*args,**kwargs):
        serializer_data = request.POST
        serializer = CustomUserSerializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


class PostListAPI(GenericAPIView,ListModelMixin,RetrieveModelMixin,CreateModelMixin):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects
    
    def get(self,request,*args,**kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)

# Create your views here.
