from rest_framework import serializers
from apps.products.models import Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Product
    fields = ['product_id', 'name', 'description', 'type', 'price']
    read_only_fields = ['product_id']
