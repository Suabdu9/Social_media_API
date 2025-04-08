from rest_framework.routers import DefaultRouter
from .views import PostViewSet, FollowViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('follow', FollowViewSet)

urlpatterns = router.urls
