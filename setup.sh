#!/bin/bash

# Create necessary directories
mkdir -p flask_app
mkdir -p django_app/items/templates/items

# Make setup scripts executable
chmod +x django_app/setup.sh

echo "Project structure created successfully!"
echo "To start the applications, run: docker-compose up --build" 