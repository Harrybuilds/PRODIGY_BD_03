from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model


User = get_user_model()


class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        email = kwargs.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExists:
            return None
        
        if user.check_password(password):
            return user
        return None 