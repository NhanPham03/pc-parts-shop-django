from rest_framework import serializers
from apps.items.models import Item

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    fields = ['item_id', 'quantity', 'product_id']
    read_only_fields = ['item_id', 'product_id']
