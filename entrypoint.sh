#!/bin/sh
set -e


echo "Applying migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput || true

echo "Creating superuser if not exists..."
python create_superuser.py || true

# Bind to Render port dynamically
PORT=${PORT:-8000}
echo "Starting Gunicorn on port $PORT..."
exec gunicorn ecommerce_api.wsgi:application --bind 0.0.0.0:$PORT --workers 3
