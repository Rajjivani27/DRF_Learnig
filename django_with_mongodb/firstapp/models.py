from django.db import models
import mongoengine as me
from mongoengine import Document,StringField,IntField,fields

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
