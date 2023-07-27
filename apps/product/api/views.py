from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import CategorySerializer
from apps.product.models import Category

class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(instance=self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Created")
        return Response(serializer.errors)