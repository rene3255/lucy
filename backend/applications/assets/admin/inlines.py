from django.contrib.contenttypes.admin import GenericTabularInline
from applications.assets.models.media_asset import MediaAsset


class MediaAssetInline(GenericTabularInline):
    model = MediaAsset
    extra = 1
