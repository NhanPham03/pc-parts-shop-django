from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    read_only_fields = ['is_staff', 'is_superuser', 'is_active', 'last_login', 'groups', 'user_permissions', 'username']
    write_only_fields = ['password']
