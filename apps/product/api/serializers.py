from rest_framework import serializers

from apps.product.models import Category, Brand, Product, ProductLine, ProductImage

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
            raise serializers.ValidationError('Type field is too long!')
        
class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        fields = '__all__'

    def validate_stock(self, value):
        if (value >= 50 or value < 0) :
            msg = 'Value must be between 0 and 50!'
            raise serializers.ValidationError(msg)
        return value
    
    def validate_price(self, value):
        if value <= 0 :
            msg = 'Price can not be lower than 0'
            raise serializers.ValidationError(msg)
        return value
    
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
