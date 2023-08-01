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
    category = models.ManyToManyField(Category)
    def __str__(self):
        return self.name
    

class Product(UUIDFY, TimeStample, models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    is_digital = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class ProductLine(UUIDFY, TimeStample, models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"Line: {self.product.name}"
    

class ProductImage(UUIDFY, TimeStample, models.Model):
    product = models.ForeignKey(ProductLine, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name
    