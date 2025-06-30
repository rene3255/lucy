from django.contrib import admin
from applications.assets.models.coin_bank_note import CoinBankNote
from applications.assets.admin.inlines import MediaAssetInline


@admin.register(CoinBankNote)
class CoinBankNoteAdmin(admin.ModelAdmin):
    inlines = [MediaAssetInline]
