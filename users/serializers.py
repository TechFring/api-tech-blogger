from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.state import token_backend

from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop("password")
        return User.objects.create(password=make_password(password), **validated_data)

    # def update(self, instance, validated_data):
    #     print("*" * 50)
    #     print(instance)
    #     print(validated_data)
    #     print("*" * 50)
    #     password = validated_data.get("password").get(
    #         "password", instance.user.password
    #     )
    #     instance.user.password = make_password(password)
    #     instance.user.save()

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "bio",
            "username",
            "photo",
            "total_publications",
            "password",
            "email",
        )
        extra_kwargs = {"password": {"write_only": True}, "email": {"write_only": True}}


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({"id": self.user.id})
        return data


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super(CustomTokenRefreshSerializer, self).validate(attrs)
        decoded_payload = token_backend.decode(data["access"], verify=True)
        user_uid = decoded_payload["user_id"]
        data.update({"id": user_uid})
        return data
