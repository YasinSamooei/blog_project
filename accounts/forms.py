from django import forms
from django.contrib.auth.forms import (PasswordChangeForm,
                                       ReadOnlyPasswordHashField)
from django.core.exceptions import ValidationError

from .models import User
from django.core import validators


class SignUpForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.TextInput(
            {'class': "email-input", "placeholder": "enter your email", 'maxlength': 50}),
    )
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "enter your full name"}))

    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        "class": "password-input", "placeholder": "enter your password"
    }))

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password')

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data.get("email")).exists():
            raise ValidationError("User with this email already exists")
        return self.cleaned_data.get("email")

    def clean_password(self):
        if len(self.cleaned_data.get("password")) < 8:
            raise ValidationError("The length of the password must be at least 8 characters")
        return self.cleaned_data.get("password")


class SignInForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder": "enter your email"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "enter your password"}))

class ChangeEmailForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder": "enter your email"}))


class CheckOTPForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your validate code'}),
                           validators=[validators.MaxLengthValidator(4)])


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput({'placeholder': "گذرواژه فعلی", 'id': "old_password"}))
    new_password1 = forms.CharField(widget=forms.PasswordInput({'placeholder': "گذرواژه جدید", 'id': "new_password1"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput({'placeholder': "تکرار گذرواژه", 'id': "new_password2"}))

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise ValidationError("گذرواژه فعلی تان اشتباه وارد شد. لطفا دوباره تلاش کنید")
        return old_password


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'full_name', 'is_active', 'is_superuser','instagram','telegram','whatsapp','image','is_staff','bio')
