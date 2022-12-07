from django.contrib.auth.models import UserManager
from django.db import models


class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = f'{self.model.USERNAME_FIELD}__iexact'
        return self.get(**{case_insensitive_username_field: username})
