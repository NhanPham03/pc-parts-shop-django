from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.items.models import Item
from apps.items.serializers import ItemSerializer

class Item_ListCreateAPIView(generics.ListCreateAPIView):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  permission_classes = [AllowAny]

class Item_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  permission_classes = [AllowAny]
