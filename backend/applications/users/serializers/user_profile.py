from rest_framework.serializers import ModelSerializer
from ..models.user_profile import UserProfile


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
