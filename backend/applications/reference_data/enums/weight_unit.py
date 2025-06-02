from django.db import models


class WeightUnit(models.TextChoices):
    GRAM = "gram", "Gramo"
    KILOGRAM = "kilogram", "Kilogramo"
    OUNCE = "onza", "Onza"
    TON = "ton", "Tonelada"
