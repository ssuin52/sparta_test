from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomModel(AbstractUser):
    class Meta:
        db_table = "custom_user"
    address = models.TextField(max_length=500, blank=True)
    bio = models.TextField(max_length=500, blank=True)

