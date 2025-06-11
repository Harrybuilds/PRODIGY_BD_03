import re
import jwt
import json
from .models import User
from .decorators import role_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from datetime import datetime, timedelta
from Access.settings import SECRET_KEY


# Create your views here.
def homepage(request):
    return JsonResponse({'message': 'home page reached'})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            age = data.get('age')
            role = data.get('role')
            password = data.get('password')


            if not name or not email or not age or not password:
                return JsonResponse({'error':'missing required data'}, status=400)

            EMAIL_REGX = r"^[^@]+@[^@]+\.[^@]+$"

            if not re.match(EMAIL_REGX, email):
                return  JsonResponse({'error':'invalid email'}, status=400)

            user = User.objects.create_user(username=name, email=email, age=age, password=password, role=role)
            return JsonResponse({
                'message': 'user created successfully',
                'user': {'id': user.id, 'username': user.username, 'email': user.email, 'age': user.age, 'role': user.role}
            }, status=201)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'bad json format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': f'{request.method} method not allowed'}, status=405)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            email = data.get('email')
            password = data.get('password')

            EMAIL_REGX = r'^[^@]+@[^@]+\.[^@]+$'

            if not email:
                return JsonResponse({'error': 'provide an email'}, status=400)

            if not re.match(EMAIL_REGX, email):
                return JsonResponse({'error': 'bad email format. Enter a valid email'}, status=400)
            
            user = authenticate(email=email, password=password)
            if not user:
                return JsonResponse(
                    {'error': 'Invalid credentials. Please recheck your credentials and try again'},
                    status=401
                    )

            payload = {
                'user_id': str(user.id),
                'email': user.email,
                'role': user.role,
                'exp': datetime.utcnow() + timedelta(seconds=3600)
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
            return JsonResponse({
                'success': f'{user.username} logged in successfully. Dashboad displayed',
                'token': token
            }, status=200)

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'bad json format'}, status=401)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def profile_view(request):
    if request.user and request.user.is_authenticated:
        return JsonResponse({'message': f'welcome {request.user.username}'})
    return JsonResponse({'error': 'Unauthorized'}, status=401)


@role_required(['admin'])
def admin_only_view(request):
    return JsonResponse({'message': 'welcome admin'})


@role_required(['staff'])
def staff_only_view(request):
    return JsonResponse({'message': 'welcome staff'})

@role_required(['admin', 'staff'])
def staffs_view(request):
    return JsonResponse({'message': f'welcome {request.user.role}'})

@role_required(['admin', 'staff', 'user'])
def all_user_view(request):
    return JsonResponse({'message': f'welcome {request.user.role}'})