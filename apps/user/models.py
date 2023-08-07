from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid

from django.db.models.query import QuerySet


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        admin = 'admin', 'admin'
        regular = 'regular', 'regular'
        golden = 'golden', 'golden'

    base_role = Role.admin

    id = models.UUIDField(primary_key=True,
                          unique=True,
                          default=uuid.uuid4)
    age = models.PositiveIntegerField(null=True)
    phone = models.PositiveIntegerField(null=True)

    role = models.CharField(max_length=10, choices=Role.choices)

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='db_index')
        ]
    
    def save(self, *args, **kwargs):
        if not self.role:
            self.role = self.base_role
        return super().save(*args, **kwargs)
        

class RegularUserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=CustomUser.Role.regular)


class RegularUser(CustomUser):
    base_role = CustomUser.Role.regular
    objects = RegularUserManager()
    class Meta:
        proxy = True


class GoldenUserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=CustomUser.Role.golden)


class GoldenUser(CustomUser):
    base_role = CustomUser.Role.golden
    objects = GoldenUserManager()
    class Meta:
        proxy = True