from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # Movie-related URLs
    path('', views.movies_list, name='movies_list'),
    path('<slug:slug>/', views.movie_detail, name='movie_detail'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('category/', views.categories_list, name='categories_list'),
    
    # Series-related URLs
    path('series/', views.series_list, name='series_list'),
    path('series/<slug:slug>/', views.series_detail, name='series_detail'),
    path('series/<slug:series_slug>/episode/<int:episode_number>/', views.episode_detail, name='episode_detail'),
    
    # Search
    path('search/', views.search, name='search'),
]