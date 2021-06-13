from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Publication, Tag, Save
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    GetPublicationSerializer,
    PublicationSerializer,
    TagSerializer,
    SaveSerializer,
)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        return [IsAdminUser()]

    @action(methods=["get"], detail=True)
    def publicacoes(self, request, pk=None):
        tag = self.get_object()
        queryset = Publication.objects.filter(tags__id=tag.id)

        page = self.paginate_queryset(queryset)
        serializer = GetPublicationSerializer(
            page, many=True, context={"request": request}
        )

        if page is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def list(self, request: Request, *args, **kwargs):
        keyword = request.query_params.get("keyword")
        if keyword == "random":
            publications = Publication.objects.all().order_by("?")[:3]
            serializer = GetPublicationSerializer(
                publications, many=True, context={"request": request}
            )
            return Response(serializer.data)
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetPublicationSerializer
        return PublicationSerializer


class SaveViewSet(viewsets.ModelViewSet):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ["post", "delete", "head", "options", "trace"]
