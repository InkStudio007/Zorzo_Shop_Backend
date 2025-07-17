from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, SizeViewSet, ProductSizeViewSet, ImageViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'sizes', SizeViewSet)
router.register(r'productsizes', ProductSizeViewSet)
router.register(r'images', ImageViewSet)


urlpatterns = [
    path('', include(router.urls))
]