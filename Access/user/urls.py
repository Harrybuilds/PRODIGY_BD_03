from django.urls import path
from . import views

urlpatterns = [
    path('home', views.homepage, name='homepage'),
    path('register/', views.register, name='new_user'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='protect'),
    path('admin_only/', views.admin_only_view, name='admin_only_view'),
    path('staff_only/', views.staff_only_view, name='staff_only_view'),
    path('staffs/', views.staffs_view, name='staffs_view'),
    path('all_users/', views.all_user_view, name='all_user_view')
]