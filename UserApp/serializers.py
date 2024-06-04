from rest_framework import serializers

from UserApp.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Пароль не совпадает!"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"]
        )

        user.set_password(validated_data["password1"])
        user.save()

        return user
