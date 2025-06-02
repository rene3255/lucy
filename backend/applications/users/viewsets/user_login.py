from rest_framework import viewsets, status
from applications.users.serializers.login import LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from applications.users.serializers.user_info import UserInfoSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Autenticación de usuarios"])
class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    http_method_names = ["post"]  # collection-base-model-implementation

    def create(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token
            return Response(
                {
                    "status": "success",
                    "user": UserInfoSerializer(user).data,
                    "refresh": str(refresh),
                    "access": str(access),
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
