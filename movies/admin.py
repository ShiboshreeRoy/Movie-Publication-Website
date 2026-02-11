from django.contrib import admin
from .models import Category, Actor, Director, Movie, Series, Episode, Advertisement


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date']
    search_fields = ['name']


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date']
    search_fields = ['name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'director', 'category', 'release_date', 'status', 'views_count', 'created_at']
    list_filter = ['status', 'category', 'release_date', 'created_at']
    search_fields = ['title', 'director__name']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'release_date'


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'director', 'category', 'release_date', 'status', 'seasons_count', 'created_at']
    list_filter = ['status', 'category', 'release_date', 'created_at']
    search_fields = ['title', 'director__name']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'release_date'


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['series', 'episode_number', 'title', 'release_date', 'created_at']
    list_filter = ['series', 'release_date', 'created_at']
    search_fields = ['title', 'series__title']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'release_date'


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'ad_type', 'is_active', 'start_date', 'end_date', 'created_at']
    list_filter = ['ad_type', 'is_active', 'start_date', 'end_date']
    search_fields = ['title']
    date_hierarchy = 'created_at'
