from rest_framework import serializers
from apps.receipts.models import Receipt

class ReceiptSerializer(serializers.ModelSerializer):
  class Meta:
    model = Receipt
    fields = ['receipt_id', 'created_at', 'total', 'cart_id', 'user_id']
    read_only_fields = ['receipt_id', 'created_at', 'cart_id', 'user_id']
