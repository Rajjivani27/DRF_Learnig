from django.contrib.auth.backends import BaseBackend
from .models import CustomUser
from django.core.exceptions import ObjectDoesNotExist
from mongoengine.errors import DoesNotExist

class MongoEngineBackend(BaseBackend):
    def authenticate(self, request, email = None, password = None, **kwargs):
        print("I am here")
        try:
            user = CustomUser.objects.get(email = email)
            if user.check_password(password):
                return user
        except DoesNotExist:
            return None
    
    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(id=user_id)
        except DoesNotExist:
            return None