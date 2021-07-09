from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import AuthRegisterViewSet, UserViewSet, AuthLoginViewSet


router = DefaultRouter()
router.register("auth/criar-conta", AuthRegisterViewSet)
router.register("usuarios", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/login/", AuthLoginViewSet.as_view(), name="auth_login"),
    path("auth/login/refresh/", TokenRefreshView.as_view(), name="auth_refresh"),
]
