from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.products.models import Product
from apps.products.serializers import ProductSerializer

class Product_ListCreateAPIView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [AllowAny]

class Product_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [AllowAny]
