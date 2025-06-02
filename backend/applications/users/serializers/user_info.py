from rest_framework import serializers
from applications.users.models.users import User


class UserInfoSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "role",
            "email",
            "first_name",
            "last_name",
            "full_name",
        )

    def get_full_name(self, obj) -> str:
        return f"{obj.first_name} {obj.last_name}".strip()
