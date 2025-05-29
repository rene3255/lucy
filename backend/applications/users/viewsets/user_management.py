from rest_framework import viewsets
from rest_framework.response import Response
from applications.permissions.is_lucy_employee import IsLucyEmployee
from applications.users.serializers.user_registration import UserRegistrationSerializer
from applications.users.serializers.user_detail import UserDetailSerializer
from applications.users.models.users import User
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Gestión de usuarios"])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsLucyEmployee]
    http_method_names = ["get", "put", "patch"]

    def get_queryset(self):
        return User.objects.all()

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
