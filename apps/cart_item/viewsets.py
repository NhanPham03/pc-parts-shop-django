from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.cart_item.models import CartItem
from apps.cart_item.serializers import CartItemSerializer

class CartItemViewSets(viewsets.ModelViewSet):
  queryset = CartItem.objects.all()
  serializer_class = CartItemSerializer
  permission_classes = [AllowAny]
