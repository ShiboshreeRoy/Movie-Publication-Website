from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from movies.models import Category


class Command(BaseCommand):
    help = 'Initialize the website with basic data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--create-superuser',
            action='store_true',
            help='Create a superuser account',
        )

    def handle(self, *args, **options):
        self.stdout.write('Initializing website setup...')
        
        # Create default categories
        categories = [
            'Action', 'Comedy', 'Drama', 'Horror', 'Romance', 
            'Sci-Fi', 'Thriller', 'Documentary', 'Animation', 'Adventure'
        ]
        
        for cat_name in categories:
            category, created = Category.objects.get_or_create(
                name=cat_name,
                defaults={'name': cat_name, 'slug': cat_name.lower()}
            )
            if created:
                self.stdout.write(f'Created category: {cat_name}')
            else:
                self.stdout.write(f'Category already exists: {cat_name}')
        
        # Optionally create a superuser
        if options['create_superuser']:
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser('admin', 'admin@example.com', 'admin')
                self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
            else:
                self.stdout.write('Superuser already exists')
        
        self.stdout.write(
            self.style.SUCCESS('Website setup completed successfully!')
        )