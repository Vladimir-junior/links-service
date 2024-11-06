from typing import Optional, Any

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager as BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, email: str, password: Optional[str], **extra_fields: Any):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: Optional[str] = None, password: Optional[str] = None, **extra_fields: Any):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email: Optional[str] = None, password: Optional[str] = None, **extra_fields: Any):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    username = None
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(_("password"), max_length=150)

    def __str__(self):
        return self.email
