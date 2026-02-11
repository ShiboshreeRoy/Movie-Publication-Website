from django.contrib import admin
from .models import Rating, Review, Download, WatchHistory, UserProfile


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_type', 'content_object', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['user__username', 'movie__title', 'series__title', 'episode__title']
    
    def content_type(self, obj):
        if obj.movie:
            return f"Movie: {obj.movie.title}"
        elif obj.series:
            return f"Series: {obj.series.title}"
        elif obj.episode:
            return f"Episode: {obj.episode.title}"
        return "Unknown"
    
    def content_object(self, obj):
        return obj.movie or obj.series or obj.episode


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'content_type', 'content_object', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'title', 'movie__title', 'series__title', 'episode__title']
    
    def content_type(self, obj):
        if obj.movie:
            return f"Movie: {obj.movie.title}"
        elif obj.series:
            return f"Series: {obj.series.title}"
        elif obj.episode:
            return f"Episode: {obj.episode.title}"
        return "Unknown"
    
    def content_object(self, obj):
        return obj.movie or obj.series or obj.episode


@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_type', 'content_object', 'download_date', 'ip_address']
    list_filter = ['download_date']
    search_fields = ['user__username', 'movie__title', 'episode__title']
    
    def content_type(self, obj):
        if obj.movie:
            return f"Movie: {obj.movie.title}"
        elif obj.episode:
            return f"Episode: {obj.episode.title}"
        return "Unknown"
    
    def content_object(self, obj):
        return obj.movie or obj.episode


@admin.register(WatchHistory)
class WatchHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_type', 'content_object', 'watched_at', 'progress']
    list_filter = ['watched_at', 'progress']
    search_fields = ['user__username', 'movie__title', 'episode__title']
    
    def content_type(self, obj):
        if obj.movie:
            return f"Movie: {obj.movie.title}"
        elif obj.episode:
            return f"Episode: {obj.episode.title}"
        return "Unknown"
    
    def content_object(self, obj):
        return obj.movie or obj.episode


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'preferred_language', 'country']
    search_fields = ['user__username', 'country']
