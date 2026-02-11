#!/bin/bash

echo "Setting up Movie Publication Website..."

# Create media directory
mkdir -p media
mkdir -p static

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running migrations..."
python3 manage.py makemigrations
python3 manage.py migrate

echo "Creating superuser (optional)..."
read -p "Do you want to create a superuser now? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    python3 manage.py createsuperuser
fi

echo "Setup complete!"
echo "To run the development server, use: python3 manage.py runserver"