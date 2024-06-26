from rest_framework import serializers
from apps.cart_items.models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = CartItem
    fields = '__all__'
