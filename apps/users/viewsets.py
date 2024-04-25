from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apps.users.models import User
from apps.users.serializers import UserSerializer

class UserViewSets(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny]

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    
    if serializer.is_valid():
      user = serializer.save()
      password = serializer.validated_data.get('password')

      if password:
        user.set_password(password)
        user.save()
      return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)

    if serializer.is_valid():
      user = serializer.save()
      password = serializer.validated_data.get('password')
      
      if not password:
        original_user = User.objects.get(pk=user.pk)
        user.set_password(original_user.password)
        user.save()
      return Response(status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
