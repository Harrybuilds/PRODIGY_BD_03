from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4 as uuid

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'ADMIN'),
        ('staff', 'STAFF'),
        ('user', 'USER')
    )
    id = models.UUIDField(primary_key=True, unique=True, default=uuid())
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']