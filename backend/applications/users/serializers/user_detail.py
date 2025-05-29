from rest_framework import serializers
from .user_profile import UserProfileSerializer
from ..models.users import User


class UserDetailSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,  # Never include in responses
        required=False,  # Allow updates without requiring a password
        style={"input_type": "password"},  # For browsable API
    )
    full_name = serializers.SerializerMethodField(read_only=True)
    profile = UserProfileSerializer(required=False)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "full_name",
            "first_name",
            "last_name",
            "email",
            "password",
            "role",
            "is_active",
            "profile",
        )
        read_only_fields = ["full_name"]

    def get_full_name(self, obj) -> str:
        return f"{obj.first_name} {obj.last_name}"

    def update(self, instance, validated_data):
        # Extract password from validated_data (if provided)
        password = validated_data.pop("password", None)

        # Hash the password (if present)
        if password:
            instance.set_password(password)  # Uses Django's hashing

        profile_data = validated_data.pop("profile", {})
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        profile = getattr(instance, "profile", None)
        if profile and profile_data:
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()
        instance.refresh_from_db()
        return instance
