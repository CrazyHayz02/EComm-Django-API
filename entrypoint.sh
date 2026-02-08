#!/bin/sh
set -e

echo "Waiting for database..."
counter=0
until python manage.py migrate --check >/dev/null 2>&1 || [ $counter -eq 10 ]; do
  sleep 3
  counter=$((counter+1))
done

if [ $counter -eq 10 ]; then
  echo "Database not ready, exiting"
  exit 1
fi

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
