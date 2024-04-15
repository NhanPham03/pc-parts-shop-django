from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.accounts.models import Account
from apps.accounts.serializers import AccountSerializer

class AccountViewSets(viewsets.ModelViewSet):
  queryset = Account.objects.all()
  serializer_class = AccountSerializer
  permission_classes = [AllowAny]
