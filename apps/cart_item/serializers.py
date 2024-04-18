from rest_framework import serializers
from apps.cart_item.models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = CartItem
    fields = '__all__'
