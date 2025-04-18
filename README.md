# Web Applications with Flask, Django, and Docker Compose

This project demonstrates the implementation of web applications using Flask and Django frameworks, containerized with Docker Compose.

## Project Structure
```
.
├── flask_app/           # Flask application
├── django_app/          # Django application
├── docker-compose.yml   # Docker Compose configuration
└── README.md           # This file
```

## Features

### Flask Application
- Simple "Hello, World!" homepage
- Form to accept user's name and age
- Basic error handling

### Django Application
- Homepage displaying a list of items
- Admin panel for item management
- Form to add new items

### Docker Setup
- Containerized Flask and Django applications
- Docker Compose for orchestration
- Separate ports for each application

## Running the Project

1. Make sure you have Docker and Docker Compose installed
2. Clone this repository
3. Run the following command:
   ```bash
   docker-compose up --build
   ```
4. Access the applications:
   - Flask app: http://localhost:5000
   - Django app: http://localhost:8000

## Development

### Flask App
- Located in `flask_app/`
- Requirements: `flask_app/requirements.txt`

### Django App
- Located in `django_app/`
- Requirements: `django_app/requirements.txt`

## License
MIT 