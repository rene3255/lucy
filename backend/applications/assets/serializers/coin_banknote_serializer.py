from rest_framework import serializers
from applications.assets.models.coin_bank_note import CoinBankNote


class CoinBankNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinBankNote
        fields = "__all__"
