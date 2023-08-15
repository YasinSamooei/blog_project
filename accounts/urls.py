from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
app_name = 'account'
urlpatterns = [

    # path('sign-in/', views.SignInView.as_view(), name='sign-in'),
    # path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    # path('verify-otp/', views.CheckOTPView.as_view(), name='verify-otp'),


    path('logout/', LogoutView.as_view(next_page='home:main'), name='logout'),
]