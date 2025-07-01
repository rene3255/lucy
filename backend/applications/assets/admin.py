from django.contrib import admin
from applications.assets.models.metals import Metal
from applications.assets.models.coin_bank_note import CoinBankNote
from .models.media_asset import MediaAsset
from .models.content import Content

# Register your models here.

admin.site.register(Metal)
admin.site.register(CoinBankNote)
admin.site.register(Content)
admin.site.register(MediaAsset)
