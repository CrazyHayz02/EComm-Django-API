#!/bin/bash

echo "Starting entrypoint script..."

# Wait for database to be ready (optional, useful if DB is on cloud)
# Replace 10 with retries, adjust host if needed
counter=0
until python manage.py showmigrations >/dev/null 2>&1 || [ $counter -eq 10 ]; do
  echo "Waiting for DB..."
  sleep 3
  counter=$((counter+1))
done

# Apply database migrations
echo "Applying migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if it doesn't exist
echo "Creating superuser if not exists..."
python create_superuser.py

print("DATABASE ENGINE:", DATABASES["default"]["ENGINE"])
print("DATABASE NAME:", DATABASES["default"]["NAME"])

# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn ecommerce_api.wsgi:application --bind 0.0.0.0:8000 --workers 3
