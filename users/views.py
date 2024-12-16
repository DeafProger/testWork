from rest_framework.permissions import (IsAuthenticated, AllowAny, 
                                        BasePermission)
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers, status
from rest_framework.response import Response
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'is_active',)


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password',)


class UserProfileSerializer(serializers.ModelSerializer):
        model = User
        fields = ('email',)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    default_serializer = UserSerializer
    serializers = {
        'create': UserCreateSerializer,
        'retrieve': UserProfileSerializer,
        'update': UserProfileSerializer,
    }

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        match self.action:
            case 'create':
                permission_classes = [AllowAny]
            case 'list':
                permission_classes = [IsAuthenticated, IsSuperUser]
            case _:
                permission_classes = [IsAuthenticated, IsOwner | IsSuperUser]

        return [permission() for permission in permission_classes]


class IsOwner(BasePermission):
    message = 'You is not page Owner.'

    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsSuperUser(BasePermission):
    message = 'You is not superUser.'

    def has_permission(self, request, view):
        return request.user.is_superuser
