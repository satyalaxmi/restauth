from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(verbose_name="email", max_length=50, null=True)
    phone_num = models.CharField(max_length=50, null=True)
    course = models.CharField(max_length=20, null=True)
