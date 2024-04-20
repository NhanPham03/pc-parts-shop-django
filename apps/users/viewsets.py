from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.users.models import User
from apps.users.serializers import UserSerializer

class UserViewSets(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny]

  def perform_create(self, serializer):
    user = serializer.save()
    password = serializer.validated_data.get('password')

    if password:
      user.set_password(password)
      user.save()

  def perform_update(self, serializer):
    user = serializer.save()
    password = serializer.validated_data.get('password')
    
    if password:
      user.set_password(password)
      user.save()
