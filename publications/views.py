from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Publication, Saved, Tag
from .serializers import (
    GetPublicationSerializer,
    PublicationSerializer,
    RetrieveSavedSerializer,
    TagSerializer,
)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    http_method_names = ["get", "head", "options", "trace"]

    @action(methods=["get"], detail=True)
    def publicacoes(self, request, pk=None):
        tag = self.get_object()
        queryset = Publication.objects.filter(tags__id=tag.id, user__is_active=True)

        page = self.paginate_queryset(queryset)
        serializer = GetPublicationSerializer(
            page, many=True, context={"request": request}
        )

        if page is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.filter(user__is_active=True)

    def list(self, request: Request, *args, **kwargs):
        keyword = request.query_params.get("keyword")
        if keyword == "random":
            publications = self.queryset.order_by("?")[:3]
            serializer = GetPublicationSerializer(
                publications, many=True, context={"request": request}
            )
            return Response(serializer.data)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        keyword = request.query_params.get("keyword")
        is_owner = request.user.id == instance.user.id
        if keyword == "owner" and not is_owner:
            data = {"detail": "Você não tem permissão para executar essa ação."}
            return Response(data, status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetPublicationSerializer
        return PublicationSerializer


class SavedViewSet(viewsets.ModelViewSet):
    queryset = Saved.objects.all()
    serializer_class = RetrieveSavedSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["post", "delete", "head", "options", "trace"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
