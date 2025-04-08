from django.shortcuts import render
from rest_framework import viewsets  # For creating ViewSets
from rest_framework.permissions import IsAuthenticated  # Permission classes
from .models import Post, Follow  # Import models
from .serializers import PostSerializer, FollowSerializer  # Import the serializers
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
