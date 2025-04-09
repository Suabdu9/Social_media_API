from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  # Permission classes
from .models import Post, Follow, Like, Comment, Notification, DirectMessage, UserProfile
from .serializers import PostSerializer, FollowSerializer, LikeSerializer, CommentSerializer, NotificationSerializer, DirectMessageSerializer, UserProfileSerializer, UserRegistrationSerializer, UserLoginSerializer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

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

class UserProfileViewSet(viewsets.ModelViewSet, APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        profile = get_object_or_404(UserProfile, user__id=user_id)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, user_id):
        profile = get_object_or_404(UserProfile, user__id=user_id)
        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile updated successfully!"})
        return Response(serializer.errors, status=400)
    
class UserRegistrationViewSet(viewsets.ModelViewSet, APIView):
    serializer_class = UserRegistrationSerializer
    authentication_classes = []  # No authentication required
    permission_classes = []
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'message': 'User registered successfully!', 'token': token.key}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class UserLoginViewSet(viewsets.ModelViewSet):
    serializer_class = UserLoginSerializer  # Specify the serializer class

    authentication_classes = []  # No authentication required for login
    permission_classes = []  # No permissions required for login

    def create(self, request):
        serializer = self.serializer_class(data=request.data)  # Validate the input
        if serializer.is_valid():
            user = serializer.validated_data['user']  # Retrieve the authenticated user
            token, _ = Token.objects.get_or_create(user=user)  # Generate or retrieve the user's token
            return Response({'message': 'Login successful!', 'token': token.key})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)