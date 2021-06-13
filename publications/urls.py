from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PublicationViewSet, TagViewSet


router = DefaultRouter()
router.register("comentarios", CommentViewSet)
router.register("publicacoes", PublicationViewSet)
router.register("tags", TagViewSet)
