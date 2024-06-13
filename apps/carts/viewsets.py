from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.carts.models import Cart
from apps.carts.serializers import CartSerializer

class CartViewSet(viewsets.ModelViewSet):
  queryset = Cart.objects.all()
  serializer_class = CartSerializer
  permission_classes = [AllowAny]
