from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

from users.managers import CustomUserManager


class User(AbstractUser):
    USER_TYPE = [
        ('normal', 'normal'),
        ('silver', 'silver'),
        ('gold', 'gold'),
    ]
    username = models.CharField(max_length=45, unique=True)
    email = models.EmailField('email address', unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE, null=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_created=True)
    modified_time = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
