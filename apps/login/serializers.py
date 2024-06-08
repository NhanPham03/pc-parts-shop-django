from django.contrib.auth import authenticate
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, attrs):
    username = attrs.get('username')
    password = attrs.get('password')

    user = authenticate(request=self.context.get('request'), username=username, password=password)

    if not user:
      raise serializers.ValidationError("Invalid username or password")
    
    return user
