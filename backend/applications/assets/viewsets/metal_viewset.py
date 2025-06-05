from rest_framework import viewsets, status
from rest_framework.response import Response
from applications.assets.models.metals import Metal
from applications.permissions.permissions import IsAdminUser, IsRegularUser
from applications.assets.serializers.metal_serializer import MetalSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Gestión de Activos (Metales, Monedas y Billetes)"])
class MetalViewSet(viewsets.ModelViewSet):
    queryset = Metal.objects.all()
    permission_classes = [IsAdminUser, IsRegularUser]
    serializer_class = MetalSerializer

    def get_queryset(self):
        return super().get_queryset().active()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
