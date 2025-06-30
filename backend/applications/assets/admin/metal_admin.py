from django.contrib import admin
from applications.assets.models.metals import Metal
from applications.assets.admin.inlines import MediaAssetInline


@admin.register(Metal)
class MetalAdmin(admin.ModelAdmin):
    inlines = [MediaAssetInline]
