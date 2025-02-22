from django.contrib import admin
from .models import LatestNews, BlogInsights

@admin.register(LatestNews)
class LatestNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'has_image', 'has_video', 'created_at')
    search_fields = ('title', 'description')

    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True

    def has_video(self, obj):
        return bool(obj.video_url)
    has_video.boolean = True

@admin.register(BlogInsights)
class BlogInsightsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'has_image', 'has_video', 'created_at')
    search_fields = ('title', 'description')

    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True

    def has_video(self, obj):
        return bool(obj.video_url)
    has_video.boolean = True