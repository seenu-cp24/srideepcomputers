from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'sku', 'description', 'category__name']
    ordering_fields = ['price', 'created_at', 'name']

    def get_queryset(self):
        qs = Product.objects.all()
        # optional: allow inactive filtering via query param ?active=true
        active = self.request.query_params.get('active')
        if active is not None:
            if active.lower() in ['true', '1']:
                qs = qs.filter(is_active=True)
            elif active.lower() in ['false', '0']:
                qs = qs.filter(is_active=False)
        return qs

    # example custom action to change stock
    @action(detail=True, methods=['post'])
    def adjust_stock(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        amount = int(request.data.get('amount', 0))
        product.stock = max(0, product.stock + amount)
        product.save()
        return Response({'stock': product.stock}, status=status.HTTP_200_OK)
