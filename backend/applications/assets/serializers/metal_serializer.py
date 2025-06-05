from rest_framework import serializers
from applications.assets.models.metals import Metal


class MetalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metal
        fields = "__all__"
