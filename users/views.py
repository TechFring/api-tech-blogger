from publications.models import Publication
from publications.permissions import IsOwnerOrReadOnly, IsOwner
from publications.serializers import GetPublicationSerializer
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
    http_method_names = ["get", "put", "patch", "delete", "head", "options", "trace"]

    def get_permissions(self):
        keyword = self.request.query_params.get("keyword")
        # if keyword == "owner":
        #     return [IsOwner()]
        return [IsOwnerOrReadOnly()]

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
