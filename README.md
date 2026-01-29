# E-commerce API (Django REST Framework)

A production-style **E-commerce REST API** built with **Django** and **Django REST Framework**.
This project demonstrates real-world backend engineering practices, including authentication, permissions, rate limiting, pagination, and clean API design.

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

## 📦 Project Structure

```text
├── ecommerce_api/
│ ├── ecommerce_api/
│ │   ├── settings.py
│ │   ├── urls.py
│ │   └── wsgi.py
│ ├── products/
│ │   ├── models.py
│ │   ├── serializers.py
│ │   ├── views.py
│ │   ├── permissions.py
│ │   └── urls.py
│ └── manage.py
├── requirments.txt
└── README.md
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

## 🛍️ Product API Endpoints

| Method | Endpoint            | Description      | Auth   |
| ------ | ------------------- | ---------------- | ------ |
| GET    | /api/products/      | List products    | Public |
| GET    | /api/products/{id}/ | Retrieve product | Public |
| POST   | /api/products/      | Create product   | Admin  |
| PUT    | /api/products/{id}/ | Update product   | Admin  |
| DELETE | /api/products/{id}/ | Delete product   | Admin  |

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

## 🧠 Why This Project Matters

This project demonstrates:

* Backend API design
* Secure authentication & authorization
* Scalable response handling
* Defensive programming practices

These are **core competencies evaluated in Google SWE & Security Engineer interviews**.

---

## 🔜 Next Steps (Planned)

* Cart & Order models
* Checkout flow
* Automated tests (pytest)
* Swagger / OpenAPI documentation
* Dockerization
* CI/CD pipeline
* Cloud deployment (Google Cloud Run)

---

## 📄 License

MIT License
