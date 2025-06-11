from django.http import JsonResponse
from functools import wraps


def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user = getattr(request, 'user', None)
            if user and user.is_authenticated and user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            return JsonResponse({'error': 'Forbidden'}, status=403)
        return wrapper
    return decorator