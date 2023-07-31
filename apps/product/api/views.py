from rest_framework.response import Response
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from apps.product.models import Category, Brand, Product


# class CategoryViewSet(viewsets.ViewSet):
#     queryset = Category.objects.all()
#     lookup_field = 'name'

#     @extend_schema(responses=CategorySerializer)
#     def list(self, request):
#         serializer = CategorySerializer(instance=self.queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response("Created")
#         return Response(serializer.errors)
    
#     def retrieve(self, request, name):
#         instance = Category.objects.get(name=name)
#         serializer = CategorySerializer(instance=instance)
#         return Response(serializer.data)
    
#     def update(self, request, name):
#         instance = Category.objects.get(name=name)
#         serializer = CategorySerializer(instance=instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response('Updated')
#         return Response(serializer.errors)    
    
#     def destroy(self, request, pk):
#         instance = Category.objects.get(name=name)
#         instance.delete()
#         return Response("Deleted")
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    lookup_field = 'name'
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        serializer = CategorySerializer(instance=self.queryset, many=True)
        return Response(serializer.data)

class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.all()
    lookup_field = 'name'

    @extend_schema(responses=BrandSerializer) 
    def list(self, request):
        serializer = BrandSerializer(instance=self.queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Created', status=201)
        return Response(serializer.errors)
    
    def retrieve(self, request, name):
        instance = Brand.objects.get(name=name)
        serializer = BrandSerializer(instance=instance)
        return Response(serializer.data)
    
    def update(self, request, pk):
        instance = Brand.objects.get(pk=pk)
        serializer = BrandSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Updated')
        return Response(serializer.errors)
    
    def destroy(self, request, pk):
        instance = Brand.objects.get(pk=pk)
        instance.delete()
        return Response("Deleted")
    

class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)    
    def list(self, request):
        serializer = ProductSerializer(instance=self.queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Created')
        return Response(serializer.errors)
    
    def update(self, request, pk):
        instance = Product.objects.get(pk=pk)
        serializer = ProductSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Updated')
        return Response(serializer.errors)
    
    def retrieve(self, request, pk):
        instance = Product.objects.get(pk=pk)
        serializer = ProductSerializer(instance=instance)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        instance = Product.objects.get(pk=pk)
        instance.delete()
        return Response("Deleted")