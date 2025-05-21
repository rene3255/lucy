from django.db import models
from applications.abstracts.models.global_abastract_model import AbstractModel


class Country(AbstractModel):
    country = models.CharField(max_length=50, unique=True)
    country_code = models.CharField(max_length=4, unique=True, null=True, blank=True)

    class Meta:
        db_table = "countries"

    def __str__(self) -> str:
        return f"{self.country_code} | {self.country}"
