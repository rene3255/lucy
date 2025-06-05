from django.contrib.auth import logout
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from applications.permissions.permissions import IsLucyEmployee
from applications.users.serializers.user_registration import UserRegistrationSerializer
from applications.users.serializers.user_detail import UserDetailSerializer
from applications.users.models.users import User
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Autenticación de usuarios"])
class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.none()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "User crated successfully",
                    "user": UserRegistrationSerializer(user).data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=False,
        methods=["post"],
        permission_classes=[IsAuthenticated],
    )
    def logout(self, request):
        logout(request)
        return Response(
            {
                "status": "success",
                "message": "You have been logged out",
            },
            status=status.HTTP_200_OK,
        )
