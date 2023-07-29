from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from apps.product.api.views import CategoryViewSet, BrandViewSet, ProductViewSet

router = DefaultRouter()
router.register(r"category", viewset=CategoryViewSet, basename='category')
router.register(r"brand", viewset=BrandViewSet, basename="brand")
router.register(r"product", viewset=ProductViewSet, basename="product")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
]
