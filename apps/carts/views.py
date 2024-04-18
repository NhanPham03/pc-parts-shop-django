from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.carts.models import Cart
from apps.carts.serializers import CartSerializer

class Cart_ListCreateAPIView(generics.ListCreateAPIView):
  queryset = Cart.objects.all()
  serializer_class = CartSerializer
  permission_classes = [AllowAny]

class Cart_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Cart.objects.all()
  serializer_class = CartSerializer
  permission_classes = [AllowAny]
