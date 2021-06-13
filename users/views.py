from publications.models import Publication, Saved
from publications.permissions import IsOwnerOrReadOnly
from publications.serializers import GetPublicationSerializer, SavedSerializer
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .models import User
from .serializers import (
    CustomTokenObtainPairSerializer,
    CustomTokenRefreshSerializer,
    UserSerializer,
)


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ["get", "put", "patch", "delete", "head", "options", "trace"]

    @action(methods=["GET"], detail=True)
    def salvos(self, request, pk=None):
        user = self.get_object()
        queryset = Saved.objects.filter(user_id=user.id)

        page = self.paginate_queryset(queryset)
        serializer = SavedSerializer(page, many=True, context={"request": request})

        if page is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)

    @action(methods=["GET"], detail=True)
    def publicacoes(self, request, pk=None):
        user = self.get_object()
        queryset = Publication.objects.filter(user_id=user.id)

        page = self.paginate_queryset(queryset)
        serializer = GetPublicationSerializer(
            page, many=True, context={"request": request}
        )

        if page is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)


class AuthViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = [
        "post",
        "head",
        "options",
        "trace",
    ]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer
