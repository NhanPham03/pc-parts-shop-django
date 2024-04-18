from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.accounts.models import Account
from apps.accounts.serializers import AccountSerializer

class Account_ListCreateAPIView(generics.ListCreateAPIView):
  queryset = Account.objects.all()
  serializer_class = AccountSerializer
  permission_classes = [AllowAny]

class Account_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Account.objects.all()
  serializer_class = AccountSerializer
  permission_classes = [AllowAny]
