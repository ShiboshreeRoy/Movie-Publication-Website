from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Avg
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Movie, Series, Episode, Category, Advertisement
from user_interactions.models import Rating, Review


def display_ads():
    """Display active advertisements"""
    active_ads = Advertisement.objects.filter(is_active=True).filter(
        start_date__lte=timezone.now(),
        end_date__gte=timezone.now()
    )
    return {'active_ads': active_ads}


def movies_list(request):
    """Display a list of all movies"""
    movies = Movie.objects.filter(status='published').order_by('-created_at')
    
    # Apply filters if present
    category_id = request.GET.get('category')
    if category_id:
        movies = movies.filter(category_id=category_id)
    
    search_query = request.GET.get('search')
    if search_query:
        movies = movies.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    
    # Pagination
    paginator = Paginator(movies, 12)  # Show 12 movies per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    advertisements = Advertisement.objects.filter(is_active=True)
    
    context = {
        'movies': page_obj,
        'categories': categories,
        'advertisements': advertisements,
        'current_category': category_id,
        'search_query': search_query,
    }
    return render(request, 'movies/list.html', context)


def movie_detail(request, slug):
    """Display details for a specific movie"""
    movie = get_object_or_404(Movie, slug=slug, status='published')
    
    # Increment view count
    movie.views_count += 1
    movie.save(update_fields=['views_count'])
    
    # Get related content
    related_movies = Movie.objects.filter(
        category=movie.category, 
        status='published'
    ).exclude(id=movie.id)[:6]
    
    # Get user's rating if logged in
    user_rating = None
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(user=request.user, movie=movie).first()
    
    # Get average rating
    avg_rating = Rating.objects.filter(movie=movie).aggregate(Avg('rating'))['rating__avg']
    
    # Get reviews
    reviews = Review.objects.filter(movie=movie).order_by('-created_at')
    
    advertisements = Advertisement.objects.filter(is_active=True)
    
    context = {
        'movie': movie,
        'related_movies': related_movies,
        'user_rating': user_rating,
        'avg_rating': avg_rating,
        'reviews': reviews,
        'advertisements': advertisements,
    }
    return render(request, 'movies/detail.html', context)


def series_list(request):
    """Display a list of all series"""
    series = Series.objects.filter(status='published').order_by('-created_at')
    
    # Apply filters if present
    category_id = request.GET.get('category')
    if category_id:
        series = series.filter(category_id=category_id)
    
    search_query = request.GET.get('search')
    if search_query:
        series = series.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    
    # Pagination
    paginator = Paginator(series, 12)  # Show 12 series per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    advertisements = Advertisement.objects.filter(is_active=True)
    
    context = {
        'series_list': page_obj,
        'categories': categories,
        'advertisements': advertisements,
        'current_category': category_id,
        'search_query': search_query,
    }
    return render(request, 'movies/series_list.html', context)


def series_detail(request, slug):
    """Display details for a specific series"""
    series = get_object_or_404(Series, slug=slug, status='published')
    
    # Get episodes
    episodes = Episode.objects.filter(series=series).order_by('episode_number')
    
    # Get related content
    related_series = Series.objects.filter(
        category=series.category, 
        status='published'
    ).exclude(id=series.id)[:6]
    
    # Get user's rating if logged in
    user_rating = None
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(user=request.user, series=series).first()
    
    # Get average rating
    avg_rating = Rating.objects.filter(series=series).aggregate(Avg('rating'))['rating__avg']
    
    # Get reviews
    reviews = Review.objects.filter(series=series).order_by('-created_at')
    
    advertisements = Advertisement.objects.filter(is_active=True)
    
    context = {
        'series': series,
        'episodes': episodes,
        'related_series': related_series,
        'user_rating': user_rating,
        'avg_rating': avg_rating,
        'reviews': reviews,
        'advertisements': advertisements,
    }
    return render(request, 'movies/series_detail.html', context)


def episode_detail(request, series_slug, episode_number):
    """Display details for a specific episode"""
    series = get_object_or_404(Series, slug=series_slug, status='published')
    episode = get_object_or_404(Episode, series=series, episode_number=episode_number)
    
    # Get related episodes
    other_episodes = Episode.objects.filter(series=series).exclude(id=episode.id).order_by('episode_number')
    
    # Get user's rating if logged in
    user_rating = None
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(user=request.user, episode=episode).first()
    
    # Get average rating
    avg_rating = Rating.objects.filter(episode=episode).aggregate(Avg('rating'))['rating__avg']
    
    # Get reviews
    reviews = Review.objects.filter(episode=episode).order_by('-created_at')
    
    advertisements = Advertisement.objects.filter(is_active=True)
    
    context = {
        'series': series,
        'episode': episode,
        'other_episodes': other_episodes,
        'user_rating': user_rating,
        'avg_rating': avg_rating,
        'reviews': reviews,
        'advertisements': advertisements,
    }
    return render(request, 'movies/episode_detail.html', context)


def categories_list(request):
    """Display a list of all categories"""
    categories = Category.objects.all()
    advertisements = Advertisement.objects.filter(is_active=True)
    
    context = {
        'categories': categories,
        'advertisements': advertisements,
    }
    return render(request, 'movies/categories.html', context)


def category_detail(request, slug):
    """Display movies and series in a specific category"""
    category = get_object_or_404(Category, slug=slug)
    
    movies = Movie.objects.filter(category=category, status='published')
    series = Series.objects.filter(category=category, status='published')
    
    # Pagination
    paginator_movies = Paginator(movies, 12)  # Show 12 movies per page
    page_number_movies = request.GET.get('page_movies')
    page_obj_movies = paginator_movies.get_page(page_number_movies)
    
    paginator_series = Paginator(series, 12)  # Show 12 series per page
    page_number_series = request.GET.get('page_series')
    page_obj_series = paginator_series.get_page(page_number_series)
    
    advertisements = Advertisement.objects.filter(is_active=True)
    
    context = {
        'category': category,
        'movies': page_obj_movies,
        'series': page_obj_series,
        'advertisements': advertisements,
    }
    return render(request, 'movies/category_detail.html', context)


def search(request):
    """Search for movies and series"""
    query = request.GET.get('q')
    
    if query:
        movies = Movie.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query),
            status='published'
        )
        series = Series.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query),
            status='published'
        )
    else:
        movies = Movie.objects.none()
        series = Series.objects.none()
    
    # Pagination
    paginator_movies = Paginator(movies, 12)  # Show 12 movies per page
    page_number_movies = request.GET.get('page_movies')
    page_obj_movies = paginator_movies.get_page(page_number_movies)
    
    paginator_series = Paginator(series, 12)  # Show 12 series per page
    page_number_series = request.GET.get('page_series')
    page_obj_series = paginator_series.get_page(page_number_series)
    
    advertisements = Advertisement.objects.filter(is_active=True)
    
    context = {
        'query': query,
        'movies': page_obj_movies,
        'series': page_obj_series,
        'advertisements': advertisements,
    }
    return render(request, 'movies/search_results.html', context)