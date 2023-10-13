from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import FileExtensionValidator
from uuid import uuid4


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=14, unique=True)
    pasport_seria = models.CharField(max_length=2)
    pasport_number = models.CharField(max_length=7)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name



