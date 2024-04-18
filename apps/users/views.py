from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.users.models import User
from apps.users.serializers import UserSerializer

class User_ListCreateAPIView(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny]

class User_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny]
