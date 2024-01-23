import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser





class UserManager(BaseUserManager):
    def create_user(self, email, username, phone_number=None, national_code=None, password=None, **extra_fields):
        user = self.model(email=email, username=username, phone_number=phone_number, national_code=national_code,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        for field in ['phone_number', 'national_code']:
            extra_fields.pop(field, None)

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'مرد'),
        ('F', 'زن'),

    ]
    email = models.EmailField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    national_code = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.username}"



class OTPRequest(models.Model):
    request_id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4())
    PHONE=models.CharField(max_length=10)
    receiver=models.CharField(max_length=20)
    password=models.CharField(max_length=4)
    created=models.DateTimeField(auto_now_add=True,editable=False)