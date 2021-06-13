from rest_framework.routers import DefaultRouter

from .views import UserViewSet, AuthViewSet


router = DefaultRouter()
router.register("auth/criar-conta", AuthViewSet)
router.register("usuarios", UserViewSet)
