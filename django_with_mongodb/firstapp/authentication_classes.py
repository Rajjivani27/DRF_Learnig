from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from mongoengine.errors import DoesNotExist
from .models import CustomUser

class CustomJWTAuthetication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token.get('user_id')

        if user_id is None:
            raise InvalidToken("Token contained no recongnizable user identification")
        
        try:
            user = CustomUser.objects.get(id = user_id)
        except DoesNotExist:
            raise InvalidToken("User Not Found")
        
        return user