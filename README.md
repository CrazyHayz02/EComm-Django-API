# E-commerce API (Django REST Framework)

A production-style **E-commerce REST API** built with **Django** and **Django REST Framework**.
This project demonstrates real-world backend engineering practices, including authentication, permissions, rate limiting, pagination, and clean API design.

---
## 🔗 Live URL
**API Live URL:** [https://ecomm-django-api.onrender.com/](https://ecomm-django-api.onrender.com/)
---

## 🚀 Features (Implemented So Far)

### ✅ Core API

* RESTful architecture
* JSON-based request/response handling
* Clean separation of models, serializers, views, and permissions

### ✅ Authentication

* JWT authentication using `djangorestframework-simplejwt`
* Secure login & token refresh endpoints
* Protected routes for authenticated users

### ✅ Authorization & Permissions

* Public **read-only** access to products
* **Admin-only** create/update/delete actions
* Custom permission class (`IsAdminOrReadOnly`)

### ✅ Rate Limiting (Throttling)

* Anonymous users: limited requests per minute
* Authenticated users: higher request limits
* Protection against abuse and brute-force attacks

### ✅ Pagination

* Page-number pagination is enabled globally
* Scalable responses for large datasets
* Frontend-friendly metadata (`count`, `next`, `previous`)

### ✅ Filtering & Ordering

* Server-side filtering using `django-filter`
* Ordering by fields such as price and creation date

---

## 🧱 Tech Stack

* **Python 3.11+**
* **Django 5**
* **Django REST Framework**
* **PostgreSQL** (SQLite for local dev)
* **JWT Authentication**
* **django-filter**
* **Postman** (API testing)

---

## 📦 Docker Deployment

```bash
docker build -t e-commerce-api .
docker run -p 8000:8000 e-commerce-api
```

## 📦 Project Structure

```text
└── 📁ecommerce_api
    └── 📁cart
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── serializers.py
        ├── services.py
        ├── tests.py
        ├── views.py
    └── 📁ecommerce_api
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        ├── wsgi.py
    └── 📁orders
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── serializers.py
        ├── services.py
        ├── tests.py
        ├── views.py
    └── 📁products
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── permissions.py
        ├── serializers.py
        ├── tests.py
        ├── throttles.py
        ├── urls.py
        ├── views.py
    ├── db.sqlite3
    └── manage.py
```

---

## 🔐 Authentication Flow

### Obtain JWT Token

```http
POST /api/token/
```

Request body:

```json
{
  "username": "user",
  "password": "password"
}
```

Response:

```json
{
  "access": "<jwt_access_token>",
  "refresh": "<jwt_refresh_token>"
}
```

### Refresh Token

```http
POST /api/token/refresh/
```
---

## 📚 API Documentation (OpenAPI / Swagger)

This API is fully documented using OpenAPI (Swagger) via `drf-spectacular`.

### Interactive API Docs (Swagger UI)
```http
/api/docs/
```

- Browse all available endpoints
- View request/response schemas
- Test authenticated endpoints directly in the browser
- JWT authentication supported via Swagger UI

### OpenAPI Schema (JSON)
``` http
/api/schema/
```
- Machine-readable OpenAPI schema
- Can be used for client generation, API gateways, or tooling

The documentation is automatically generated from serializers,
views, and permissions, ensuring it stays in sync with the codebase.

---


## 🛍️ Product API Endpoints

| Method | Endpoint            | Description      | Auth   |
| ------ | ------------------- | ---------------- | ------ |
| GET    | /api/products/      | List products    | Public |
| GET    | /api/products/{id}/ | Retrieve product | Public |
| POST   | /api/products/      | Create product   | Admin  |
| PUT    | /api/products/{id}/ | Update product   | Admin  |
| DELETE | /api/products/{id}/ | Delete product   | Admin  |

---

## 🛒 Cart & Order API Endpoints

| Method | Endpoint              | Description                  | Auth          |
| ------ | --------------------- | ---------------------------- | ------------- |
| GET    | /api/cart/            | Retrieve current user’s cart | Authenticated |
| POST   | /api/cart/add/        | Add product to cart          | Authenticated |
| DELETE | /api/cart/remove/     | Remove product from cart     | Authenticated |
| POST   | /api/orders/checkout/ | Checkout cart → create order | Authenticated |
| GET    | /api/orders/          | List user’s orders           | Authenticated |
| GET    | /api/orders/{id}/     | Retrieve specific order      | Authenticated |

### Request Example — Add to Cart

```http
POST /api/cart/add/
Authorization: Bearer <access_token>
Content-Type: application/json
```

```json
{
  "product_id": 5,
  "quantity": 2
}
```

### Response Example

```json
{
  "cart_item_id": 12,
  "product": {
    "id": 5,
    "name": "Gaming Laptop",
    "price": 1999.99
  },
  "quantity": 2,
  "total_price": 3999.98
}
```

### Request Example — Checkout Cart

```http
POST /api/orders/checkout/
Authorization: Bearer <access_token>
```

### Response Example

```json
{
    "id": 4,
    "user": "user",
    "items": [
        {
            "id": 6,
            "product": 7,
            "product_name": "SolarCell Max",
            "quantity": 20,
            "price": "1099.00"
        }
    ],
    "total_price": "21980.00",
    "status": "PENDING",
    "created_at": "2026-02-01T00:58:33.064621Z"
```

---

## ⚙️ Service Layer & Business Logic

All critical operations are implemented in a **service layer** (`services.py`) to separate business logic from views:

* `add_to_cart(user, product_id, quantity)` — validates stock, updates cart, creates `CartItem`
* `remove_from_cart(user, product_id)` — deletes item from cart
* `checkout_cart(user)` — converts cart items to order, updates stock, clears cart, calculates total price

> Demonstrates **clean architecture**, a skill Google evaluates in SWE interviews.

---

## ⚙️ Pagination Example

```http
GET /api/products/?page=2
```

Response:

```json
{
  "count": 125,
  "next": "/api/products/?page=3",
  "previous": "/api/products/?page=1",
  "results": [...]
}
```

---

## 🚦 Rate Limiting

| User Type     | Limit            |
| ------------- | ---------------- |
| Anonymous     | 10 requests/min  |
| Authenticated | 100 requests/min |

Throttled response:

```json
{
  "detail": "Request was throttled. Expected available in 60 seconds."
}
```

---

## 🧪 Local Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

---

## Deployment
This project is prepared for Docker-based deployment and CI/CD.

---

## 🧠 Why This Project Matters

This project demonstrates:

* Backend API design
* Secure authentication & authorization
* Scalable response handling
* Defensive programming practices
* Clean separation of concerns (service layer)

---

## 📄 License

MIT License
