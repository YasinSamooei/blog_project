from django.contrib.auth.models import AbstractBaseUser
from persiantools.jdatetime import JalaliDate
from django.utils import timezone
from .managers import UserManager
from django.db import models


class User(AbstractBaseUser):

    email = models.EmailField('آدرس ایمیل', max_length=255,unique=True)
    full_name = models.CharField('نام و نام خانوادگی', max_length=55)
    image = models.ImageField('تصویر', upload_to='images/users', null=True, blank=True)
    bio = models.CharField('بیوگرافی', null=True, blank=True , max_length=500)
    instagram =models.URLField('آدرس اینستاگرام',null=True,blank=True)
    telegram =models.URLField('آدرس تلگرام',null=True,blank=True)
    whatsapp =models.URLField('آدرس واتساپ',null=True,blank=True)

    date_joined = models.DateTimeField('تاریخ عضویت', auto_now_add=True)
    is_active = models.BooleanField('فعال', default=True)
    is_staff = models.BooleanField('کارمند', default=False)
    is_author = models.BooleanField(default=False)
    is_superuser = models.BooleanField('ادمین', default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["full_name"]

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'

    def get_jalali_date(self):
        return JalaliDate(self.date_joined, locale=('fa')).strftime('%c')

    get_jalali_date.short_description = 'تاریخ ثبت نام'


    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Otp(models.Model):
    email = models.CharField('آدرس ایمیل', max_length=50)
    full_name = models.CharField('نام و نام خانوادگی', max_length=50)
    password = models.CharField('گذرواژه', max_length=1000)
    code = models.CharField('کد اعتبارسنجی', max_length=5)
    token = models.CharField('توکن اعتبار سنجی', max_length=50)
    expiration = models.DateTimeField('زمان انقضا', null=True, blank=True)

    class Meta:
        verbose_name_plural = "کدهای اعتبارسنجی"
        verbose_name = "کد اعتبارسنجی"

    # Check OTP code is still valid or not.
    def is_not_expired(self):
        if self.expiration >= timezone.localtime(timezone.now()):
            return True
        else:
            return False

    def __str__(self):
        return self.email