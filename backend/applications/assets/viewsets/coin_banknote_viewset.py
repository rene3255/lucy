from rest_framework import viewsets, status
from rest_framework.response import Response
from applications.assets.models.coin_bank_note import CoinBankNote
from applications.permissions.permissions import IsAdminUser, IsRegularUser
from applications.assets.serializers.coin_banknote_serializer import (
    CoinBankNoteSerializer,
)
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Gestión de Monedas y Billetes"])
class CoinBankNoteViewSet(viewsets.ModelViewSet):
    queryset = CoinBankNote.objects.all()
    permission_classes = [IsAdminUser, IsRegularUser]
    serializer_class = CoinBankNoteSerializer

    def get_queryset(self):
        return super().get_queryset().active()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
