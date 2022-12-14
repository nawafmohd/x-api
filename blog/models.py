from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    def __str__(self):
        return self.title