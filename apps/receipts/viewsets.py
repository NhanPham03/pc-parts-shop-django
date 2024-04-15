from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.receipts.models import Receipt
from apps.receipts.serializers import ReceiptSerializer

class ReceiptViewSets(viewsets.ModelViewSet):
  queryset = Receipt.objects.all()
  serializer_class = ReceiptSerializer
  permission_classes = [AllowAny]
