from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from .behaviours import TimeStample, UUIDFY

import uuid


class Category(UUIDFY, TimeStample, MPTTModel):
    name = models.CharField(max_length=150)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class Brand(UUIDFY, TimeStample, models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    

class Product(UUIDFY, TimeStample, models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=150)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey("category", on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name
