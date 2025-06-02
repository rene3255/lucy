from django.db import models
from applications.abstracts.models.global_abastract_model import AbstractModel


class MetalType(AbstractModel):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "metals_type"
        verbose_name = "Metal Type"
        verbose_name_plural = "Metal Types"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name}, is_active={self.is_active})"
