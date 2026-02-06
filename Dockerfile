FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy the requirements from ecommerce_api folder
COPY ecommerce_api/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# Copy the entire app
COPY ecommerce_api /app

# Collect static files
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Run server
ENTRYPOINT ["./entrypoint.sh"]