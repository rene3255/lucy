from django.db import models


class ContentTypeName(models.TextChoices):
    PHOTO = "photo", "Fotografía"
    VIDEO = "video", "Video"
    PDF = "documento", "Archivo PDF"
    TEXT = "text", "Texto"
