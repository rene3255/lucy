from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from applications.abstracts.managers.global_abstract_manager import AbstractManager
from applications.abstracts.models.assets_base_model import AbstractAssetBaseModel
from applications.reference_data.enums.coin_or_bank_note import CoinOrBankNote
from applications.reference_data.models.country import Country


class CoinBankNote(AbstractAssetBaseModel):
    coin_banknote = models.CharField(max_length=20, choices=CoinOrBankNote.choices)
    year = models.IntegerField(
        validators=[MinValueValidator(1400), MaxValueValidator(datetime.now().year)]
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="coin_country",
        null=True,
        blank=True,
    )
    denomination = models.CharField(max_length=200, blank=True, null=True)

    objects = AbstractManager()

    class Meta:
        db_table = "coinsbanknotes"
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title

    def __repr__(self):
        return f"{type(self).__name__}(title={self.title}, coin_banknote={self.coin_banknote},year={self.year})"
