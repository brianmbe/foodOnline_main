from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have a username')

        user = self.model(
            email self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_supperuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email=email),
            username=username,
            password=password,
            last_name=last_name,
            first_name=first_name
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self.db)
        return user


class User(AbstractUser):
    pass
