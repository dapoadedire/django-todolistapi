from rest_framework import serializers
from authentication.models import User


class RegisterSerializer(serializers.Serializer):
     username = serializers.CharField(max_length=100, min_length=6)
     email = serializers.EmailField(max_length=120)
     password = serializers.CharField(max_length=100, min_length=8, write_only=True)
  

     class Meta:
         model = User
         fields = ["username", "email", "password"]
     def create(self, validated_data):
         return User.objects.create_user(**validated_data)




