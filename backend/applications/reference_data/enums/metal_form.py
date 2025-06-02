from django.db import models


class MetalForm(models.TextChoices):
    BAR = "bar", "Bar"
    INGOT = "ingot", "Lingote"
    GRAIN = "grain", "Grano"
    WIRE = "wire", "Cable"
    SCRAP = "scrap", "Chatarra"
    ROUNDED = "rounded", "Circular"
    SHEET = "sheet", "Lamina"
