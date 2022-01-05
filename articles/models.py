from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)