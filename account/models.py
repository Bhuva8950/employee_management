from django.db import models

from django.contrib.auth.models import AbstractUser


ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('employee', 'Employee'),
    ('manager', 'Manager'),
]

class User(AbstractUser):
    role = models.CharField(max_length = 20 , default = 'employee', choices = ROLE_CHOICES)
