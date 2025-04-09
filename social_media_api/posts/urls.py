from rest_framework.routers import DefaultRouter
from .views import PostViewSet, FollowViewSet, LikeViewSet, CommentViewSet, NotificationViewSet, DirectMessageViewSet, UserProfileViewSet, UserRegistrationViewSet, UserLoginViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('follow', FollowViewSet, basename='follow')
router.register('likes', LikeViewSet, basename='like')
router.register('comments', CommentViewSet, basename='comment')
router.register('notifications', NotificationViewSet, basename='notification')
router.register('messages', DirectMessageViewSet, basename='message')
router.register('profile', UserProfileViewSet, basename='user-profile')
router.register('register', UserRegistrationViewSet, basename='register')
router.register('login', UserLoginViewSet, basename='login')

urlpatterns = router.urls
