from rest_framework import serializers
from rest_framework.authentication import authenticate


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        if email and password:
            user = authenticate(
                request=self.context.get("request"),
                email=email,
                password=password,
            )
            if not user:
                raise serializers.ValidationError("No credentials were provided.")

            if not user.is_active:
                raise serializers.ValidationError("Imposible logearse")
        else:
            raise serializers.ValidationError("Must include email and password")

        data["user"] = user
        return data
