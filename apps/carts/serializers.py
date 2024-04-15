from rest_framework import serializers
from apps.carts.models import Cart

class CartSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cart
    fields = ['cart_id', 'user_id', 'updated_at']
    read_only_fields = ['cart_id', 'user_id', 'updated_at']
