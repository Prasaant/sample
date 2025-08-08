from django.db import models

class UserSession(models.Model):
    session_id = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ChatMessage(models.Model):
    session = models.ForeignKey(UserSession, on_delete=models.CASCADE)
    is_user = models.BooleanField()
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
