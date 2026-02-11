from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Rating, Review, Download, WatchHistory, UserProfile
from movies.models import Movie, Series, Episode


@login_required
def rate_movie(request, movie_id):
    """Rate a movie"""
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=movie_id)
        rating_value = int(request.POST.get('rating', 0))
        
        if 1 <= rating_value <= 5:
            # Check if user already rated this movie
            rating, created = Rating.objects.update_or_create(
                user=request.user,
                movie=movie,
                defaults={'rating': rating_value}
            )
            
            if created:
                messages.success(request, f"You rated '{movie.title}' with {rating_value} stars!")
            else:
                messages.info(request, f"Your rating for '{movie.title}' has been updated to {rating_value} stars!")
        else:
            messages.error(request, "Invalid rating value. Please select 1-5 stars.")
    
    return redirect('movies:movie_detail', slug=movie.slug)


@login_required
def rate_series(request, series_id):
    """Rate a series"""
    if request.method == 'POST':
        series = get_object_or_404(Series, id=series_id)
        rating_value = int(request.POST.get('rating', 0))
        
        if 1 <= rating_value <= 5:
            # Check if user already rated this series
            rating, created = Rating.objects.update_or_create(
                user=request.user,
                series=series,
                defaults={'rating': rating_value}
            )
            
            if created:
                messages.success(request, f"You rated '{series.title}' with {rating_value} stars!")
            else:
                messages.info(request, f"Your rating for '{series.title}' has been updated to {rating_value} stars!")
        else:
            messages.error(request, "Invalid rating value. Please select 1-5 stars.")
    
    return redirect('movies:series_detail', slug=series.slug)


@login_required
def rate_episode(request, episode_id):
    """Rate an episode"""
    if request.method == 'POST':
        episode = get_object_or_404(Episode, id=episode_id)
        rating_value = int(request.POST.get('rating', 0))
        
        if 1 <= rating_value <= 5:
            # Check if user already rated this episode
            rating, created = Rating.objects.update_or_create(
                user=request.user,
                episode=episode,
                defaults={'rating': rating_value}
            )
            
            if created:
                messages.success(request, f"You rated '{episode.title}' with {rating_value} stars!")
            else:
                messages.info(request, f"Your rating for '{episode.title}' has been updated to {rating_value} stars!")
        else:
            messages.error(request, "Invalid rating value. Please select 1-5 stars.")
    
    return redirect('movies:episode_detail', series_slug=episode.series.slug, episode_number=episode.episode_number)


@login_required
def add_review_movie(request, movie_id):
    """Add a review for a movie"""
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=movie_id)
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        
        if title and content:
            # Check if user already reviewed this movie
            review, created = Review.objects.update_or_create(
                user=request.user,
                movie=movie,
                defaults={
                    'title': title,
                    'content': content
                }
            )
            
            if created:
                messages.success(request, f"Your review for '{movie.title}' has been added!")
            else:
                messages.info(request, f"Your review for '{movie.title}' has been updated!")
        else:
            messages.error(request, "Please provide both title and content for your review.")
    
    return redirect('movies:movie_detail', slug=movie.slug)


@login_required
def add_review_series(request, series_id):
    """Add a review for a series"""
    if request.method == 'POST':
        series = get_object_or_404(Series, id=series_id)
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        
        if title and content:
            # Check if user already reviewed this series
            review, created = Review.objects.update_or_create(
                user=request.user,
                series=series,
                defaults={
                    'title': title,
                    'content': content
                }
            )
            
            if created:
                messages.success(request, f"Your review for '{series.title}' has been added!")
            else:
                messages.info(request, f"Your review for '{series.title}' has been updated!")
        else:
            messages.error(request, "Please provide both title and content for your review.")
    
    return redirect('movies:series_detail', slug=series.slug)


@login_required
def add_review_episode(request, episode_id):
    """Add a review for an episode"""
    if request.method == 'POST':
        episode = get_object_or_404(Episode, id=episode_id)
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        
        if title and content:
            # Check if user already reviewed this episode
            review, created = Review.objects.update_or_create(
                user=request.user,
                episode=episode,
                defaults={
                    'title': title,
                    'content': content
                }
            )
            
            if created:
                messages.success(request, f"Your review for '{episode.title}' has been added!")
            else:
                messages.info(request, f"Your review for '{episode.title}' has been updated!")
        else:
            messages.error(request, "Please provide both title and content for your review.")
    
    return redirect('movies:episode_detail', series_slug=episode.series.slug, episode_number=episode.episode_number)


@login_required
def download_movie(request, movie_id):
    """Handle movie download"""
    movie = get_object_or_404(Movie, id=movie_id)
    
    # Record download
    download, created = Download.objects.get_or_create(
        user=request.user,
        movie=movie,
        defaults={
            'ip_address': get_client_ip(request)
        }
    )
    
    if created:
        messages.success(request, f"'{movie.title}' has been added to your downloads!")
    else:
        messages.info(request, f"You have already downloaded '{movie.title}'.")
    
    # Return the movie file for download
    if movie.video_file:
        from django.http import FileResponse
        response = FileResponse(
            open(movie.video_file.path, 'rb'), 
            content_type='video/mp4'
        )
        response['Content-Disposition'] = f'attachment; filename="{movie.title}.mp4"'
        return response
    else:
        messages.error(request, f"'{movie.title}' is not available for download.")
        return redirect('movies:movie_detail', slug=movie.slug)


@login_required
def download_episode(request, episode_id):
    """Handle episode download"""
    episode = get_object_or_404(Episode, id=episode_id)
    
    # Record download
    download, created = Download.objects.get_or_create(
        user=request.user,
        episode=episode,
        defaults={
            'ip_address': get_client_ip(request)
        }
    )
    
    if created:
        messages.success(request, f"'{episode.title}' has been added to your downloads!")
    else:
        messages.info(request, f"You have already downloaded '{episode.title}'.")
    
    # Return the episode file for download
    if episode.video_file:
        from django.http import FileResponse
        response = FileResponse(
            open(episode.video_file.path, 'rb'), 
            content_type='video/mp4'
        )
        response['Content-Disposition'] = f'attachment; filename="{episode.title}.mp4"'
        return response
    else:
        messages.error(request, f"'{episode.title}' is not available for download.")
        return redirect('movies:episode_detail', series_slug=episode.series.slug, episode_number=episode.episode_number)


@login_required
def watch_history(request):
    """Display user's watch history"""
    watch_history = WatchHistory.objects.filter(user=request.user).select_related(
        'movie', 'episode'
    ).order_by('-watched_at')
    
    context = {
        'watch_history': watch_history,
    }
    return render(request, 'user_interactions/watch_history.html', context)


@login_required
@require_POST
def mark_progress(request, content_type, content_id):
    """Mark progress for a movie or episode"""
    progress = float(request.POST.get('progress', 0))
    
    if content_type == 'movie':
        content = get_object_or_404(Movie, id=content_id)
        watch_history, created = WatchHistory.objects.update_or_create(
            user=request.user,
            movie=content,
            defaults={'progress': progress}
        )
    elif content_type == 'episode':
        content = get_object_or_404(Episode, id=content_id)
        watch_history, created = WatchHistory.objects.update_or_create(
            user=request.user,
            episode=content,
            defaults={'progress': progress}
        )
    else:
        return JsonResponse({'success': False, 'error': 'Invalid content type'})
    
    return JsonResponse({
        'success': True, 
        'message': f'Progress saved for {content.title}'
    })


@login_required
def profile(request):
    """Display user profile"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Get user's activity
    ratings = Rating.objects.filter(user=request.user).select_related('movie', 'series', 'episode')
    reviews = Review.objects.filter(user=request.user).select_related('movie', 'series', 'episode')
    downloads = Download.objects.filter(user=request.user).select_related('movie', 'episode')
    watch_history = WatchHistory.objects.filter(user=request.user).select_related('movie', 'episode')
    
    context = {
        'profile': profile,
        'ratings': ratings,
        'reviews': reviews,
        'downloads': downloads,
        'watch_history': watch_history,
    }
    return render(request, 'user_interactions/profile.html', context)


@login_required
def edit_profile(request):
    """Edit user profile"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        # Update profile fields
        profile.preferred_language = request.POST.get('preferred_language', profile.preferred_language)
        profile.date_of_birth = request.POST.get('date_of_birth', profile.date_of_birth)
        profile.country = request.POST.get('country', profile.country)
        profile.save()
        
        # Update favorite genres
        profile.favorite_genres.clear()
        genre_ids = request.POST.getlist('favorite_genres')
        profile.favorite_genres.add(*genre_ids)
        
        messages.success(request, "Your profile has been updated!")
        return redirect('user_interactions:profile')
    
    # Prepare context for the form
    from movies.models import Category
    categories = Category.objects.all()
    
    context = {
        'profile': profile,
        'categories': categories,
    }
    return render(request, 'user_interactions/edit_profile.html', context)


def get_client_ip(request):
    """Get client IP address"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip