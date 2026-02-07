import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yourproject.settings")
django.setup()

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "SuperSecurePassword123")
    print("Superuser created")
else:
    print("Superuser already exists")


print("DATABASE ENGINE:", DATABASES["default"]["ENGINE"])
print("DATABASE NAME:", DATABASES["default"]["NAME"])