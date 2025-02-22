from django.db import models

from django.db import models
from django.core.exceptions import ValidationError

class LatestNews(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.image and not self.video_url:
            raise ValidationError("Either an image or a video URL must be provided.")
        if self.image and self.video_url:
            raise ValidationError("Please provide either an image or a video URL, not both.")

    def __str__(self):
        return self.title

class BlogInsights(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.image and not self.video_url:
            raise ValidationError("Either an image or a video URL must be provided.")
        if self.image and self.video_url:
            raise ValidationError("Please provide either an image or a video URL, not both.")

    def __str__(self):
        return self.title