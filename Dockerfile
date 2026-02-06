FROM python:3.11-slim

WORKDIR /app

# Copy the requirements from ecommerce_api folder
COPY ecommerce_api/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# Copy the entire app
COPY ecommerce_api /app

# Collect static files
RUN python manage.py collectstatic --noinput

# Run server
CMD gunicorn ecommerce_api.wsgi:application --bind 0.0.0.0:8000
