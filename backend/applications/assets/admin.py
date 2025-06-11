from django.contrib import admin
from applications.assets.models.metals import Metal
from applications.assets.models.coin_bank_note import CoinBankNote

# Register your models here.

admin.site.register(Metal)
admin.site.register(CoinBankNote)
