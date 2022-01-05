from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()        
    time = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


    def save(self, *arg, **kwargs):
        if self.slug is not None:
            self.slug = slugify(self.title)
        super().save(*arg, **kwargs)