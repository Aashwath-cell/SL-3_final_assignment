FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Make setup script executable and run initial setup
RUN chmod +x setup.sh && ./setup.sh

EXPOSE 8000

# Create a startup script
RUN echo '#!/bin/bash\npython manage.py migrate\npython manage.py runserver 0.0.0.0:8000' > /start.sh && \
    chmod +x /start.sh

CMD ["/start.sh"] 