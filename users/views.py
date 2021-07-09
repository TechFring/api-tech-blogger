from publications.models import Publication, Saved
from publications.serializers import (
    GetPublicationSerializer,
    RetrieveSavedSerializer,
    SavedSerializer,
)
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import UserSerializer


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    http_method_names = ["get", "put", "patch", "head", "options", "trace"]

    def get_permissions(self):
        if self.action == "list":
            return [IsAuthenticated()]
        return super().get_permissions()

    def list(self, request: Request, *args, **kwargs):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(serializer.data)

    @action(methods=["GET"], detail=True)
    def salvos(self, request: Request, pk=None):
        user = self.get_object()
        publication_id = request.query_params.get("publication_id")
        if publication_id:
            try:
                queryset = Saved.objects.get(
                    user_id=user.id, publication_id=publication_id
                )
                serializer = RetrieveSavedSerializer(queryset)
                return Response(serializer.data)
            except Exception:
                data = {}
                return Response(data, status.HTTP_200_OK)

        queryset = Saved.objects.filter(
            user_id=user.id, publication__user__is_active=True
        )
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


class AuthRegisterViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = [
        "post",
        "head",
        "options",
        "trace",
    ]


class AuthLoginViewSet(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs):
        username = request.data["username"]
        password = request.data["password"]

        user = User.objects.get(username=username)
        user_is_not_active = user.check_password(password) and not user.is_active

        if user_is_not_active:
            user.is_active = True
            user.save()

        return super().post(request, *args, **kwargs)
