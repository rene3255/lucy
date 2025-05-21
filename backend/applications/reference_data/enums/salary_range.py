from django.db import models


class SalaryRange(models.TextChoices):
    LOW = "bajo", "Bajo"
    MIDDLE_LOW = "medio_bajo", "Medio bajo"
    MIDDLE_HIGH = "medio_alto", "Medio alto"
    HIGH = "alto", "Alto"
    VERY_HIGH = "muy_alto", "Muy alto"
