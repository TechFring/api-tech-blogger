from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, LikeViewSet, PublicationViewSet, TagViewSet


router = DefaultRouter()
router.register("comentarios", CommentViewSet)
router.register("likes", LikeViewSet)
router.register("publicacoes", PublicationViewSet)
router.register("tags", TagViewSet)
