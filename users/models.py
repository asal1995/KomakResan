from django.contrib.auth.models import AbstractUser
from django.db import models

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
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()

    def __str__(self):
        return self.username
