import os
import django

# Must set settings BEFORE importing Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce_api.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if not password:
    raise Exception("DJANGO_SUPERUSER_PASSWORD environment variable not set!")

# Only create if missing
user, created = User.objects.get_or_create(username=username, defaults={
    "email": email,
    "is_superuser": True,
    "is_staff": True,
})

if created:
    user.set_password(password)
    user.save()
    print("Superuser created")
else:
    print("Superuser already exists")