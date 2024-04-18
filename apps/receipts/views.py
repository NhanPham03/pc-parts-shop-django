from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.receipts.models import Receipt
from apps.receipts.serializers import ReceiptSerializer

class Receipt_ListCreateAPIView(generics.ListCreateAPIView):
  queryset = Receipt.objects.all()
  serializer_class = ReceiptSerializer
  permission_classes = [AllowAny]

class Receipt_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Receipt.objects.all()
  serializer_class = ReceiptSerializer
  permission_classes = [AllowAny]
