from rest_framework import serializers
from apps.accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):
  class Meta:
    model = Account
    fields = ['account_id', 'username', 'password', 'user_id']
    read_only_fields = ['account_id', 'user_id']
