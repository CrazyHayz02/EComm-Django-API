# Dockerfile inside .github/ecommerce_api/
FROM python:3.11-slim

WORKDIR /app

# Add subfolder prefix
COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

COPY . /app

RUN python manage.py collectstatic --noinput

CMD gunicorn ecommerce_api.wsgi:application --bind 0.0.0.0:8000