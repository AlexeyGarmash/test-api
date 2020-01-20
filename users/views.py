from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated

from . import models, serializers, paginations, permissions
# Create your views here.

class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    pagination_class = paginations.UserPagination

class UserDetailView(generics.RetrieveAPIView):
    queryset = UserListView.queryset
    serializer_class = UserListView.serializer_class

class UserUpdateInfo(generics.UpdateAPIView):
    permission_classes = [permissions.UserIsOwnerPermission, IsAuthenticated]
    queryset = UserListView.queryset
    serializer_class = serializers.UserUpdateSerializer