from django.db import models
from applications.abstracts.models.global_abastract_model import AbstractModel


class Country(AbstractModel):
    country = models.CharField(max_length=50, unique=True)
    country_code = models.CharField(max_length=4, unique=True, null=True, blank=True)
    flag_url = models.URLField(blank=True, null=True)

    class Meta:
        db_table = "countries"
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ["country"]

    def __str__(self) -> str:
        return f"{self.country_code} | {self.country}"

    def __repr__(self):
        return f"{type(self).__name__}(country={self.country}, country_code={self.country_code})"
