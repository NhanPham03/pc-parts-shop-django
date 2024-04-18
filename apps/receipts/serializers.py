from rest_framework import serializers
from apps.receipts.models import Receipt

class ReceiptSerializer(serializers.ModelSerializer):
  class Meta:
    model = Receipt
    fields = '__all__'
    