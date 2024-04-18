from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.cart_item.models import CartItem
from apps.cart_item.serializers import CartItemSerializer

class CartItem_ListCreateAPIView(generics.ListCreateAPIView):
  queryset = CartItem.objects.all()
  serializer_class = CartItemSerializer
  permission_classes = [AllowAny]

class CartItem_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = CartItem.objects.all()
  serializer_class = CartItemSerializer
  permission_classes = [AllowAny]
