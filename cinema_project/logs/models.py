from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ActionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Quem fez a ação
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True) #  Data e hora da ação

    def __str__(self):
        return f"{self.user} - {self.action} - {self.timestamp}"