from django.db import models


class CoinOrBankNote(models.TextChoices):
    COIN = "coin", "Moneda"
    BANK_NOTE = "bank_note", "Papel Moneda"
