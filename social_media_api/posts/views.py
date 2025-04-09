from django.shortcuts import render
from rest_framework import viewsets  # For creating ViewSets
from rest_framework.permissions import IsAuthenticated  # Permission classes
from .models import Post, Follow, Like, Comment, Notification, DirectMessage 
from .serializers import PostSerializer, FollowSerializer, LikeSerializer, CommentSerializer, NotificationSerializer, DirectMessageSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Social Media API! Go to /api/ for the endpoints.")

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-timestamp')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    #custom filtering for comments
    def get_queryset(self):
        return self.queryset.order_by('-timestamp') 

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
class DirectMessageViewSet(viewsets.ModelViewSet):
    queryset = DirectMessage.objects.all()
    serializer_class = DirectMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(sender=self.request.user) | self.queryset.filter(receiver=self.request.user)
