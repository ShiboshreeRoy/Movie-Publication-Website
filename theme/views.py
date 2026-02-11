from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from movies.models import Movie, Series, Category


def home(request):
    """Home page view showing featured content"""
    featured_movies = Movie.objects.filter(status='published').order_by('-created_at')[:6]
    featured_series = Series.objects.filter(status='published').order_by('-created_at')[:6]
    categories = Category.objects.all()[:8]
    
    context = {
        'featured_movies': featured_movies,
        'featured_series': featured_series,
        'categories': categories,
    }
    return render(request, 'theme/home.html', context)


def about(request):
    """About page view"""
    return render(request, 'theme/about.html')


def contact(request):
    """Contact page view"""
    return render(request, 'theme/contact.html')


def register(request):
    """Simple registration view"""
    if request.method == 'POST':
        from django.contrib.auth.forms import UserCreationForm
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('home')
    else:
        from django.contrib.auth.forms import UserCreationForm
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})