from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

from .managers import CustomUserManager

# Create your models here.


class User(AbstractUser):

    objects = CustomUserManager()

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
        self.username = self.username.lower()
        if self.email and self.__class__.objects.filter(email__iexact=self.email).exclude(username=self.username).exists():
            raise ValidationError('Este e-mail já foi cadastrado.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
