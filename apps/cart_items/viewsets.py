from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.cart_items.models import CartItem
from apps.cart_items.serializers import CartItemSerializer

class CartItemViewSet(viewsets.ModelViewSet):
  queryset = CartItem.objects.all()
  serializer_class = CartItemSerializer
  permission_classes = [AllowAny]
