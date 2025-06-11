import jwt
from Access.settings import SECRET_KEY
from django.utils.deprecation import MiddlewareMixin
from .models import User


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
                request.user = User.objects.get(id=payload['user_id'])
            except (jwt.ExpiredSignatureError, jwt.DecodeError, User.DoesNotExist):
                request.user = None
        else:
            request.user = None
    
        return self.get_response(request)
   

