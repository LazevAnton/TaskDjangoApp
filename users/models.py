from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    username = models.CharField(unique=True, max_length=32)
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.get_full_name() or self.username
