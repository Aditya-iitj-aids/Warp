# Warp
FastAPI Multi-User Login System

A simple FastAPI web application with a secure login form, supporting multiple users and dynamic redirection to a protected dashboard page after successful login.

#Features
- Login page built with HTML and FastAPI
- Supports multiple hardcoded users
- Error handling for incorrect credentials
- Redirects to a dashboard after login

---

📁 Project Structure

├── main.py # FastAPI app

├── templates/

│ ├── login.html # Login form

│ └── dashboard.html # Dashboard after login

└── README.md # This file


## Instructions
Visit /login to access the login page.

Enter a valid username and password (see users_db).

On success, you'll be redirected to /dashboard.

On failure, you'll get a clear error message.


## Extra
Store users in a real database (e.g., SQLite, PostgreSQL)

Hash passwords securely using bcrypt

Use session or JWT tokens for persistent login

Add registration and logout functionality

## Tech Stack

FastAPI

Jinja2 (for HTML templating)

Uvicorn (ASGI server)
