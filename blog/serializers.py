from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Post, Comment

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')
    title = serializers.CharField(max_length=255)
    body = serializers.CharField(max_length=10000)
    # comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body')


class CommentSerializer(serializers.ModelSerializer):

    comment_by = serializers.ReadOnlyField(source='comment_by.username')

    class Meta:
        model = Comment
        fields = ('id', 'comment_body', 'comment_by', 'post')