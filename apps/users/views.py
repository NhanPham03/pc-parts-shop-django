from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.users.models import User
from apps.users.serializers import CreateUserSerializer, UpdateUserSerializer

class UserListCreate(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = CreateUserSerializer
  permission_classes = [AllowAny]

  def create(self, request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UpdateUserSerializer
  permission_classes = [AllowAny]

  def update(self, request):
    serializer = UpdateUserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
