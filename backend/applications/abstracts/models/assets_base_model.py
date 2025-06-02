from django.db import models
from applications.abstracts.managers.global_abstract_manager import AbstractManager
from .global_abastract_model import AbstractModel


class AbstractAssetBaseModel(AbstractModel):
    title = models.CharField(max_length=150, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    estimated_value = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )

    def soft_delete(self):
        self.is_active = False
        self.save()

    def restore(self):
        self.is_active = True
        self.save()

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} {self.id}"
