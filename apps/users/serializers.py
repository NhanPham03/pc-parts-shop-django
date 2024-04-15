from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['user_id', 'first_name', 'last_name', 'email', 'address', 'birthdate', 'city', 'country']
    read_only_fields = ['user_id']