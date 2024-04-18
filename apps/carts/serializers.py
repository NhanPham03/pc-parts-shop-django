from rest_framework import serializers
from apps.carts.models import Cart

class CartSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cart
    fields = '__all__'
