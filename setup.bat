@echo off
echo Creating project structure...

:: Create necessary directories
mkdir flask_app
mkdir django_app\items\templates\items

echo Project structure created successfully!
echo To start the applications, run: docker-compose up --build 