from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from .managers import UserManager
from django.db import models


class User(AbstractBaseUser):

    email = models.EmailField(max_length=255,unique=True)
    full_name = models.CharField(max_length=55)
    image = models.ImageField(upload_to='images/users', null=True, blank=True)
    bio = models.CharField(null=True, blank=True , max_length=500)
    instagram =models.URLField(null=True,blank=True)
    twitter =models.URLField(null=True,blank=True)
    linkedin =models.URLField(null=True,blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["full_name"]


    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Otp(models.Model):
    email = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    password = models.CharField(max_length=1000)
    code = models.CharField(max_length=5)
    token = models.CharField(max_length=50)
    expiration = models.DateTimeField(null=True, blank=True)

    # Check OTP code is still valid or not.
    def is_not_expired(self):
        if self.expiration >= timezone.localtime(timezone.now()):
            return True
        else:
            return False

    def __str__(self):
        return self.email