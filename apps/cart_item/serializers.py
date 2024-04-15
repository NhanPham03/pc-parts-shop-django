from rest_framework import serializers
from apps.cart_item.models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = CartItem
    fields = ['cart_id', 'item_id']
    read_only_fields = ['cart_id', 'item_id']
