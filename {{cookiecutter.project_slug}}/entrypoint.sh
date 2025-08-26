#!/bin/sh

# Generate Django project only if manage.py does not exist
if [ ! -f "manage.py" ]; then
  echo "⚙️  No Django project found, generating..."
  django-admin startproject {{cookiecutter.project_slug}} .
fi

# Apply migrations
python manage.py migrate

# Start development server
python manage.py runserver 0.0.0.0:8000
