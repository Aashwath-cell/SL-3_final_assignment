#!/bin/bash

# Create Django project
django-admin startproject myproject .

# Create items app
python manage.py startapp items

# Create migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell 