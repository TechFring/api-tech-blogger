from rest_framework.routers import DefaultRouter

from .views import UserViewSet, FollowerViewSet, AuthViewSet


router = DefaultRouter()
router.register("auth/criar-conta", AuthViewSet)
router.register("usuarios", UserViewSet)
router.register("seguidores", FollowerViewSet)
