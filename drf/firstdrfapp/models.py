from django.db import models

# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import CustomUserManager
from PIL import Image

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email= models.EmailField(unique=True)
    username = models.CharField(unique=True,max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='profile')
    name = models.CharField(max_length=50)
    user_bio = models.CharField(max_length=200,blank=True,null=True)
    profile_pic = models.ImageField(upload_to='media/',blank=True,null=True)
    dob = models.DateField()

    
class Post(models.Model):
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='posts')
    title = models.CharField(max_length=100)
    content = models.TextField()
    likes = models.ManyToManyField(CustomUser,related_name='liked_posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title
# Create your models here.
