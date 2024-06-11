from rest_framework import serializers
from apps.users.models import User

class CreateUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'address', 'birthdate', 'city', 'country']
    extra_kwargs = {
      'password': {'write_only': True, 'required': True}
    }

  def create(self, validated_data):
    password = validated_data.pop('password')
    user = User.objects.create(**validated_data)
    user.set_password(password)
    user.save()
    return user

class UpdateUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'address', 'birthdate', 'city', 'country']
    extra_kwargs = {
      'username': {'required': False},
      'password': {'write_only': True, 'required': False}
    }
  
  def update(self, instance, validated_data):
    password = validated_data.pop('password', None)
    user = super().update(instance, validated_data)
    if password:
      user.set_password(password)
    user.save()
    return user
