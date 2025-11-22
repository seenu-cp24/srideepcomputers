from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'', ProductViewSet, basename='product')  # root maps to products/

urlpatterns = [
    path('', include(router.urls)),
]
