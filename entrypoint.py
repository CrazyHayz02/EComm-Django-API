import os
import django
from django.core.management import call_command
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce_api.settings")
django.setup()

# Run migrations
call_command("migrate", interactive=False)

# Collect static files
call_command("collectstatic", interactive=False, clear=True)

# Create superuser if it doesn’t exist
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "SuperSecurePassword123")
    print("Superuser created")
else:
    print("Superuser already exists")

# Start Gunicorn
os.system("gunicorn ecommerce_api.wsgi:application --bind 0.0.0.0:8000")
