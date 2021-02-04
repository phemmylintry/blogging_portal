from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Post(models.Model):
    
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):

    post = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE)
    comment_by = models.ForeignKey(User, related_name='comment_by', on_delete=models.CASCADE)
    comment_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)