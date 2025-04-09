from rest_framework.routers import DefaultRouter
from .views import PostViewSet, FollowViewSet, LikeViewSet, CommentViewSet, NotificationViewSet, DirectMessageViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('follow', FollowViewSet)
router.register('likes', LikeViewSet, basename='like')
router.register('comments', CommentViewSet, basename='comment')
router.register('notifications', NotificationViewSet, basename='notification')
router.register('messages', DirectMessageViewSet, basename='message')

urlpatterns = router.urls
