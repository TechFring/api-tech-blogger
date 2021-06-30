from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(password=make_password(password), **validated_data)
        return user

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes("update", self, validated_data)
        info = model_meta.get_field_info(instance)

        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            elif attr == "password":
                password = make_password(value)
                setattr(instance, attr, password)
            else:
                setattr(instance, attr, value)

        instance.save()

        for attr, value in m2m_fields:
            field = getattr(instance, attr)
            field.set(value)

        return instance

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
            "date_joined",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "total_publications": {"read_only": True},
            "date_joined": {"read_only": True},
        }
