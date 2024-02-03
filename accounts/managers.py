from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom manager for the custom NewUser model below
    """

    def create_user(self, email, full_name, password=None, **other_fields):
        # Set the values to the variables for creating a user account
        if not email:
            raise ValueError("the email must be set")
        email = self.normalize_email(email)
        user = self.model(full_name=full_name, email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        # Set is_staff, is_superuser, and is_active to True as default
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("superuser must have is_staff True")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("superuser must have is_superuser True")
        if other_fields.get("is_active") is not True:
            raise ValueError("superuser must have is_active True")
        return self.create_user(email=email, password=password, **other_fields)
