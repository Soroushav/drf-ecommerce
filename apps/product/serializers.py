from rest_framework import serializers

from .models import Category, Brand, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        if str(value).startswith('category'):
            raise serializers.ValidationError('Category Should not start with the name : category!')
        
        return value
        
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, data):
        if len(data.get('type')) >= 10:
            raise serializers.ValidationError('type is too long!')
        