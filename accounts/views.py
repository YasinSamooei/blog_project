from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import (PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.core.cache import cache
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
import datetime
import pytz

from . import message
from .forms import *
from .mixins import *
from .models import *
from .otp_service import OTP


# class SignInView(generic.FormView):
#     template_name = 'accounts/sign-in.html'
#     form_class = SignInForm

#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             clean_data = form.cleaned_data
#             user = authenticate(username=clean_data['email'], password=clean_data['password'])
#             if  user is not None:
#                 login(self.request, user)
#                 return redirect('home:main')
#             else:
#                 form.add_error('email', message.Wrong_Email_Or_Password)
#         return render(request, 'accounts/sign-in.html', context={'form': form})


# class SignUpView(generic.FormView):
#     template_name = 'accounts/sign-up.html'
#     form_class = SignUpForm

#     def form_valid(self, form):
#         data = form.cleaned_data
#         otp_service = OTP()
#         otp_service.generate_otp(data['email'])
#         cache.set(key='register', value={'email': data['email'], 'password': data['password'],
#                                          'full_name': data['full_name']}, timeout=300)
#         return redirect('account:verify-otp')


# class CheckOTPView(generic.View):
#     form_class = CheckOTPForm

#     def get(self, request):
#         form = self.form_class()
#         return render(request, 'accounts/verify_otp.html', {'form': form})

#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             data_cache = cache.get(key='register')
#             otp_obj = OTP()
#             if data is None:
#                 messages.add_message(request, messages.WARNING, 'کد وجود ندارد یا نامعتبر است')
#             try:
#                 if otp_obj.verify_otp(otp=data['code'], data=data_cache['email']):
#                     user = User.objects.create_user(email=data_cache['email'], full_name=data_cache['full_name'], password=data_cache['password'])
#                     login(request, user)
#                     return redirect('home:main')
#                 else:
#                     messages.add_message(request, messages.WARNING, 'کد وجود ندارد یا نامعتبر است')
#             except:
#                 messages.add_message(request, messages.WARNING, 'کد وجود ندارد یا نامعتبر است')
#                 return render(request, 'accounts/verify_otp.html', {'form': form})

#         return render(request, 'accounts/verify_otp.html', {'form': form})


# class ChangeOTPView(generic.View):
#     form_class = CheckOTPForm

#     def get(self, request):
#         form = self.form_class()
#         return render(request, 'accounts/change-otp.html', {'form': form})

#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             data_cache = cache.get(key='change')
#             otp_obj = OTP()
#             if data is None:
#                 messages.add_message(request, messages.WARNING, 'کد وجود ندارد یا نامعتبر است')
#             try:
#                 if otp_obj.verify_otp(otp=data['code'], data=data_cache['email']):
#                     user =request.user
#                     user.email=data_cache['email']
#                     user.save()
#                     return redirect('home:main')
#                 else:
#                     messages.add_message(request, messages.WARNING, 'کد وجود ندارد یا نامعتبر است')
#             except:
#                 messages.add_message(request, messages.WARNING, 'کد وجود ندارد یا نامعتبر است')
#                 return render(request, 'accounts/change-otp.html', {'form': form})

#         return render(request, 'accounts/change-otp.html', {'form': form})

