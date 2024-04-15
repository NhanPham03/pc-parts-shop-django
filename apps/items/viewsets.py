from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.items.models import Item
from apps.items.serializers import ItemSerializer

class ItemViewSets(viewsets.ModelViewSet):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  permission_classes = [AllowAny]
