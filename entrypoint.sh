#!/bin/sh
set -e  # Exit immediately on error

# ------------------------------
# Wait for database to be ready
# ------------------------------
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

# ------------------------------
# Apply migrations
# ------------------------------
echo "Applying migrations..."
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
