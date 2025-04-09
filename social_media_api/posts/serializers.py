from rest_framework import serializers
from .models import Post, Follow, Like, Comment, Notification, DirectMessage, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id', 'user', 'timestamp']

        def validate_media(self, value):
            if value:
                # Restrict file size
                max_size = 5 * 1024 * 1024
                if value.size > max_size:
                    raise serializers.ValidationError("Media file size should not exceed 5MB.")
                # Restrict file types (e.g., images and videos only)
                allowed_types = ['image/jpeg', 'image/png', 'video/mp4']
                if value.content_type not in allowed_types:
                    raise serializers.ValidationError("Unsupported media file type.")
            return value
    

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = [ 'id', 'user', 'post']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'content', 'timestamp']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'type', 'user', 'related_post', 'related_user', 'is_read', 'timestamp']
    
class DirectMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessage
        fields = ['id', 'sender', 'receiver', 'content', 'timestamp']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'website', 'cover_photo']

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials.")
        data['user'] = user
        return data