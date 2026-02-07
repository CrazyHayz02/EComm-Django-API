FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements and install
COPY ecommerce_api/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY ecommerce_api /app

# Copy entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Start container
ENTRYPOINT ["/entrypoint.sh"]
