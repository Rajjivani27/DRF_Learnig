from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import PostSerializer,CustomUserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.views.generic import ListView,DetailView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.template import loader,TemplateDoesNotExist
from rest_framework import viewsets,views,generics
from datetime import datetime
from firstdrfapp import urls

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-created_at','-id']
    paginated_by = 10

class PostListView(ListView):
    model = Post
    template_name = 'firstdrfapp/post.html'

    def get_template_names(self):
        try:
            loader.get_template(self.template_name)
            return [self.template_name]
        except TemplateDoesNotExist:
            raise TemplateDoesNotExist(f"The provided template does not exist in system : {self.template_name}")

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self, form):
        title = form.cleaned_data['title']
        content = form.cleaned_data['content']
        
        form.instance.author = self.request.user

        self.object = form.save()
        return super().form_valid(form)
    
class PostCreateAPI(viewsets.ViewSet):
    def list(self,request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset,many=True)
        return Response(serializer.data)
    
class PostViewSet(viewsets.ViewSet):
    lookup_field = 'pk'

    @cache_page(60*60*2,key_prefix='')
    def list(self,request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset,many=True,context = {'request':request})
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        posts = Post.objects.all()
        post = get_object_or_404(posts,pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    
class CustomUserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'pk'

    def retrieve(self, request,pk=None):
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()
        user = get_object_or_404(queryset,pk=pk)
        userReturn = serializer(user)
        return Response(userReturn.data)

    
    

# Create your views here.