from rest_framework import serializers
from users.serializers import UserSerializer

from .models import Publication, Saved, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class PublicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Publication
        fields = "__all__"

    def create(self, validated_data):
        tags = validated_data.pop("tags")
        publication = Publication(**validated_data)
        publication.save()

        for tag in tags:
            publication.tags.add(tag)

        return publication


class GetPublicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Publication
        fields = "__all__"


class SavedSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    publication = GetPublicationSerializer(read_only=True)

    class Meta:
        model = Saved
        fields = "__all__"


class RetrieveSavedSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Saved
        fields = "__all__"
