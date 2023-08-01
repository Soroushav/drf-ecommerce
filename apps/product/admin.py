from django.contrib import admin
from .models import Category, Brand, Product, ProductLine, ProductImage


class ProductLineInline(admin.StackedInline):
    model = ProductLine
    extra = 1

class ProductImageInLine(admin.StackedInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline, ]

class ProductLineAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'stock']
    inlines = [ProductImageInLine,]
    
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductLine, ProductLineAdmin)
admin.site.register(ProductImage)