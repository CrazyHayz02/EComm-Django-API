#!/bin/sh
set -e  # Exit immediately on error

# ------------------------------
# Apply migrations
# ------------------------------
echo "Applying migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# ------------------------------
# Collect static files
# ------------------------------
echo "Collecting static files..."
python manage.py collectstatic --noinput || true

# ------------------------------
# Create superuser if not exists
# ------------------------------
echo "Creating superuser if it doesn't exist..."
python create_superuser.py || true

# ------------------------------
# Start Gunicorn on Render port
# ------------------------------
PORT=${PORT:-8000}  # fallback if PORT not set
echo "Starting Gunicorn on port $PORT..."
exec gunicorn ecommerce_api.wsgi:application --bind 0.0.0.0:$PORT --workers 3
