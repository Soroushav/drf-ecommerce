from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission, SAFE_METHODS
from drf_spectacular.utils import extend_schema

from .serializers import CategorySerializer, BrandSerializer, ProductSerializer, ProductLineSerializer, ProductImageSerializer
from apps.product.models import Category, Brand, Product, ProductLine, ProductImage

class IsAdminOrGoldenOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return bool((not request.user.role == 'regular') or request.method in SAFE_METHODS)

    

class SearchMixin:

    @action(detail=False, methods=['GET'])
    def search(self, request):
        queryset = self.queryset
        serializer_class = self.serializer_class
        keyword = request.query_params.get('keyword', None)

        if keyword :
            queryset = queryset.filter(name__icontains=keyword)
            serializer = serializer_class(instance=queryset, many=True)
            return Response(serializer.data)
        
        serializer = serializer_class(instance=queryset, many=True)
        return Response(serializer.data)


@extend_schema(responses=CategorySerializer)
class CategoryViewSet(viewsets.ModelViewSet, SearchMixin):
    queryset = Category.objects.all()
    lookup_field = 'name'
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrGoldenOrReadOnly,]

@extend_schema(responses=BrandSerializer)    
class BrandViewSet(viewsets.ModelViewSet, SearchMixin):
    queryset = Brand.objects.all()
    lookup_field = 'name'
    serializer_class = BrandSerializer
    permission_classes = [IsAdminOrGoldenOrReadOnly,]

@extend_schema(responses=ProductSerializer)    
class ProductViewSet(viewsets.ModelViewSet, SearchMixin):
    queryset = Product.objects.all()
    lookup_field = 'name'
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrGoldenOrReadOnly,]


@extend_schema(responses=ProductLineSerializer)  
class ProductLineViewSet(viewsets.ModelViewSet, SearchMixin):
    queryset = ProductLine.objects.all()
    serializer_class = ProductLineSerializer
    lookup_field = 'product__name'
    permission_classes = [IsAdminOrGoldenOrReadOnly,]
   
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({'message': 'Created'})
    
    
@extend_schema(responses=ProductImageSerializer)    
class ProductImageViewSet(viewsets.ModelViewSet, SearchMixin):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    lookup_field = 'name'
    permission_classes = [IsAdminOrGoldenOrReadOnly,]
  
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({'message': 'Created'})