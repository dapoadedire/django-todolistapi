from rest_framework import serializers
from authentication.models import User


class RegisterSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


