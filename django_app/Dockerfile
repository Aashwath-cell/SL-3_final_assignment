FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Initialize the database and run the server
CMD bash -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000" 