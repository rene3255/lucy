from django.db import models
from applications.abstracts.models.assets_base_model import AbstractAssetBaseModel
from applications.reference_data.enums.weight_unit import WeightUnit
from django.core.validators import MinValueValidator, MaxValueValidator
from applications.reference_data.enums.metal_form import MetalForm
from applications.reference_data.models.metals_type import MetalType
from applications.abstracts.managers.global_abstract_manager import AbstractManager


class Metal(AbstractAssetBaseModel):
    metal_type = models.ForeignKey(MetalType, on_delete=models.CASCADE)
    weight_in_grams = models.FloatField()
    weight_unit = models.CharField(
        max_length=20, choices=WeightUnit.choices, default=WeightUnit.GRAM
    )
    purity = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    certification = models.CharField(max_length=100, blank=True, null=True)
    metal_form = models.CharField(
        max_length=30,
        choices=MetalForm.choices,
        default=MetalForm.SCRAP,
    )

    objects = AbstractManager()

    class Meta:
        db_table = "metals"
        verbose_name = "Metal"
        verbose_name_plural = "Metals"

    def __str__(self) -> str:
        return f"{self.title} elaborado en {self.metal_type.name}"
