from django.db import models
from django.contrib.auth.hashers import make_password,check_password
import mongoengine as me
from mongoengine import Document,StringField,IntField,fields

class CustomUser(me.Document):
    email = me.EmailField(unique=True,required=True)
    username = StringField(unique=True,required=True)
    password = StringField(required=True)
    is_active = me.BooleanField(default=True)
    is_staff = me.BooleanField(default=False)
    is_superuser = me.BooleanField(default=False)

    def set_password(self,raw_password):
        self.password = make_password(raw_password)

    def check_password(self,raw_password):
        return check_password(raw_password,self.password)
    
    def __str__(self):
        return self.username

class Author(Document):
    name = StringField(max_length=100)

    def __str__(self):
        return self.name

class Post(Document):
    title = StringField(required=True,max_length=200)
    content = StringField()
    likes = IntField(default=0)
    author = me.ReferenceField(Author,reverse_delete_rule=me.CASCADE)

    meta = {
        'collection':'posts'
    }

    def __str__(self):
        return self.title

class Blog(Document):
    title = StringField(required=True,max_length=200)
    content = StringField()
    likes = IntField(default=0)

    meta = {
        'collection':'blogs'
    }

    def __str__(self):
        return self.title
    

# Create your models here.
