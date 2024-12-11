# app.py

import os
from django.http import HttpResponse
from django.conf import settings
from django.urls import path
from django.core.wsgi import get_wsgi_application

# Install Django before running:
# pip install django

# Create a basic Django settings structure
settings.configure(
    DEBUG=True,
    SECRET_KEY='randomsecretkey',  # Make sure to change it for production
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=['django.middleware.common.CommonMiddleware'],
    INSTALLED_APPS=['django.contrib.contenttypes'],
)

# Define a simple view
def home(request):
    return HttpResponse("Hello, this is my simple Django app!")

# URL patterns for the app
urlpatterns = [
    path('', home, name='home'),
]

# Set the WSGI application to allow Django to run as a web app
application = get_wsgi_application()

if __name__ == '__main__':
    # Django's default development server (useful for local testing)
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'runserver'])

