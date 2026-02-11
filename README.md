# Movie Publication Website

A professional movie publication website built with Django, PostgreSQL, and Tailwind CSS.

## Features

- **Admin Panel**: Admins can publish movies, TV series, and manage content
- **User Features**: Users can view, download, rate, and review movies and series
- **Advertisements**: Admins can add various types of ads (banners, popups, videos, sidebar)
- **Responsive Design**: Built with Tailwind CSS for responsive UI
- **User Profiles**: Personalized profiles with favorite genres and watch history

## Tech Stack

- Python 3.12
- Django 6.0.2
- PostgreSQL
- Tailwind CSS
- HTML5 & CSS3

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd movie-publication-website
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up PostgreSQL database:
```sql
CREATE DATABASE movie_db;
CREATE USER postgres WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE movie_db TO postgres;
```

5. Update database settings in `moviewebsite/settings.py` if needed

6. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Create a superuser:
```bash
python manage.py createsuperuser
```

8. Install and build Tailwind CSS:
```bash
python manage.py tailwind install
python manage.py tailwind build
```

9. Run the development server:
```bash
python manage.py runserver
```

## Admin Panel

Access the admin panel at `/admin/` to manage:
- Movies and TV series
- Categories and genres
- Actors and directors
- Advertisements
- User ratings and reviews

## Models Overview

- **Movie**: Movie information including title, description, release date, duration, etc.
- **Series**: TV series information with seasons and episodes
- **Episode**: Individual episodes of a series
- **Category**: Genres like Action, Drama, Comedy, etc.
- **Actor/Director**: People involved in movies/series
- **Advertisement**: Various ad formats for monetization
- **Rating**: User ratings for movies, series, and episodes
- **Review**: User-written reviews
- **Download**: Track downloads
- **WatchHistory**: Track viewing progress
- **UserProfile**: Extended user profile information

## URLs Structure

- `/` - Homepage with featured content
- `/movies/` - Browse all movies
- `/movies/<slug>/` - Movie detail page
- `/movies/series/` - Browse all series
- `/movies/series/<slug>/` - Series detail page
- `/movies/series/<slug>/episode/<number>/` - Episode detail page
- `/movies/category/<slug>/` - Movies/Series by category
- `/user/profile/` - User profile page
- `/user/watch-history/` - Watch history page

## Custom Commands

The project includes custom functionality for:
- Managing advertisements
- Processing user interactions (ratings, reviews, downloads)
- Tracking watch history

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.