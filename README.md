# Task Management API

A simple RESTful API built with Django Rest Framework that allows users to register, authenticate via JWT, and manage their personal tasks.

---

## Features

- ser Registration & JWT Authentication
- Create, Read, Update, and Delete (CRUD) tasks
- Protected endpoints using JWT
- Task ownership maintained per user

---

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: Simple JWT
- **Database**: SQLite (default)

---

## ⚙Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd task-api
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

---

## Authentication

### Obtain JWT Token

- **Endpoint**: `POST /api/token/`
- **Body (JSON)**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response**:
  ```json
  {
    "access": "<access_token>",
    "refresh": "<refresh_token>"
  }
  ```

---

## 📬 API Endpoints

| Endpoint              | Method | Description                                 |
|-----------------------|--------|---------------------------------------------|
| `/api/token/`         | POST   | Obtain access and refresh JWT tokens        |
| `/api/token/refresh/` | POST   | Refresh access token                        |
| `/tasks/`             | GET    | Get all tasks (requires auth)               |
| `/tasks/`             | POST   | Create a new task (requires auth)           |
| `/tasks/<id>/`        | GET    | Retrieve task by ID                         |
| `/tasks/<id>/`        | PUT    | Update task by ID                           |
| `/tasks/<id>/`        | DELETE | Delete task by ID                           |

---

##  Request Headers

All protected endpoints must include:

```http
Authorization: Bearer <your_jwt_access_token>
```

---

## Example Task JSON

```json
{
  "title": "Sample Task",
  "description": "This is a test task",
  "user": 1
}
```
Output

All endpoints tested and verified using Postman
---
pictures have been added in repository for reference
Demo Video
-----
https://www.youtube.com/watch?v=vMUOq3q8_a0&ab_channel=RoossoP
## Author

**Roosso P**  
📍 Chennai, India  
🎓 B.Tech – Artificial Intelligence and Data Science  
💼 Passionate about building intelligent systems and full-stack solutions!

---

