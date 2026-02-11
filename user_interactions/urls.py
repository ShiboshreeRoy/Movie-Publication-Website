from django.urls import path
from . import views

app_name = 'user_interactions'

urlpatterns = [
    # Rating and review URLs
    path('rate-movie/<int:movie_id>/', views.rate_movie, name='rate_movie'),
    path('rate-series/<int:series_id>/', views.rate_series, name='rate_series'),
    path('rate-episode/<int:episode_id>/', views.rate_episode, name='rate_episode'),
    
    # Review URLs
    path('review-movie/<int:movie_id>/', views.add_review_movie, name='add_review_movie'),
    path('review-series/<int:series_id>/', views.add_review_series, name='add_review_series'),
    path('review-episode/<int:episode_id>/', views.add_review_episode, name='add_review_episode'),
    
    # Download URLs
    path('download-movie/<int:movie_id>/', views.download_movie, name='download_movie'),
    path('download-episode/<int:episode_id>/', views.download_episode, name='download_episode'),
    
    # Watch history URLs
    path('watch-history/', views.watch_history, name='watch_history'),
    path('mark-progress/<str:content_type>/<int:content_id>/', views.mark_progress, name='mark_progress'),
    
    # User profile URLs
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]