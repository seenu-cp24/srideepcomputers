"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include  # include() is used to reference app urls

urlpatterns = [
    # Django admin panel
    path('admin/', admin.site.urls),

    # Products app API endpoints
    # All URLs defined in products/urls.py will be prefixed with /api/products/
    path('api/products/', include('products.urls')),

    # Alias for the same products endpoints
    path('products/', include('products.urls')),
]
