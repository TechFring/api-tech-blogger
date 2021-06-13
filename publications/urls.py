from rest_framework.routers import DefaultRouter

from .views import PublicationViewSet, TagViewSet, SaveViewSet


router = DefaultRouter()
router.register("publicacoes", PublicationViewSet)
router.register("tags", TagViewSet)
router.register("salvos", SaveViewSet)
