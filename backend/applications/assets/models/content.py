from django.db import models
from applications.abstracts.models.assets_base_model import AbstractModel
from applications.users.models.user_profile import UserProfile
from .media_asset import MediaAsset


class Content(AbstractModel):
    title = models.CharField(max_length=255)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True
    )
    media_asset = models.ForeignKey(MediaAsset, on_delete=models.CASCADE)

    class Meta:
        db_table = "contents"
        verbose_name = "Content"
        verbose_name_plural = "Contents"

    def __repr__(self):
        return f"Content {self.id}: {self.title}"
