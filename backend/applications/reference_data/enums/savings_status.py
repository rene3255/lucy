from django.db import models


class SavingsStatus(models.TextChoices):
    ACTIVE = "activo", "Activo"
    ACHIEVED = "logrado", "Logrado"
    ABANDONED = "abandonado", "Abandonado"
