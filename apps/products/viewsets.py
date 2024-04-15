from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.products.models import Product
from apps.products.serializers import ProductSerializer

class ProductViewSets(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [AllowAny]
