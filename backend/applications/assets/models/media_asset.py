from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from applications.reference_data.enums.content_type_name import ContentTypeName


class MediaAsset(models.Model):
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True, blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey("content_type", "object_id")
    media_url = models.URLField(null=True, blank=True)
    media_content_type = models.CharField(
        max_length=50,
        choices=ContentTypeName,
        default=ContentTypeName.PHOTO,
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "media_assets"
        verbose_name = "Digital Medium"
        verbose_name_plural = "Digital Media"

    def __str__(self):
        return self.media_url or "No image url"
