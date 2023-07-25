from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True,
                          unique=True,
                          default=uuid.uuid4)
    age = models.PositiveIntegerField(null=True)
    phone = models.PositiveIntegerField(null=True)


class Meta:
    indexes = [
        models.Index(fields=['id'], name='db_index')
    ]