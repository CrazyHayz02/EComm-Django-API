#!/bin/sh
set -e

# Wait for Postgres
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

# Run migrations safely
echo "Applying migrations..."
python manage.py migrate --noinput

# Create superuser after DB is ready
python create_superuser.py

# Start Gunicorn
PORT=${PORT:-8000}
exec gunicorn ecommerce_api.wsgi:application --bind 0.0.0.0:$PORT --workers 3
