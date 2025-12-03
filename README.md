# FastAPI Authentication & User Management API

A lightweight REST API built using FastAPI, SQLite, and SQLAlchemy, complete with secure JWT authentication, password hashing, and full User CRUD operations.

![Screenshot of all implemented FastAPI endpoints (Auth and CRUD)](img/fastapi_docs.png)

---
## Features
* **User Authentication:** Secure login and registration using OAuth2 (Password Flow) and JWT.
* **Password Security:** Passwords are hashed using `pbkdf2_sha256` before storage.
* **Database Integration:** Fully integrated with SQLite using **SQLAlchemy ORM**.
* **CRUD Operations:** Full Create, Read, Update, and Delete capabilities for user management.
* **Dependency Injection:** Clean architecture using FastAPI's dependency injection system for database sessions and current user verification.

---
## Tech Stack
<div align="center">

| Technology | Badge |
|-----------|--------|
| **Python 3.9+** | ![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white) |
| **FastAPI** | ![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi&logoColor=white) |
| **SQLite** | ![SQLite](https://img.shields.io/badge/SQLite-Database-044A64?logo=sqlite&logoColor=white) |
| **SQLAlchemy** | ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-CA3C24?logo=sqlalchemy&logoColor=white) |
| **Passlib** | ![Passlib](https://img.shields.io/badge/Passlib-Hashing-1E88E5) |
| **PyJWT** | ![PyJWT](https://img.shields.io/badge/PyJWT-Tokens-FF6F00) |
| **OAuth2PasswordBearer** | ![OAuth2](https://img.shields.io/badge/OAuth2-Bearer_Tokens-1976D2) |
| **Pydantic** | ![Pydantic](https://img.shields.io/badge/Pydantic-Validation-E92063?logo=pydantic&logoColor=white) |

</div>

---
## API Endpoints Overview
### Authentication

| Method | Endpoint       | Description                          |
|--------|----------------|--------------------------------------|
| POST   | /register      | Register a new user account.         |
| POST   | /token         | Login to receive an Access Token.    |
| GET    | /verify-token  | Check if your current token is valid.|

### User Management
| Method | Endpoint        | Description                               |
|--------|------------------|-------------------------------------------|
| GET    | /profile         | Get details of the logged-in user.        |
| GET    | /users/          | List all users (Requires Auth).           |
| GET    | /users/{id}      | Get a specific user by ID.                |
| POST   | /users/          | Create a new user (Admin function).       |
| PUT    | /users/{id}      | Update user details.                      |
| DELETE | /users/{id}      | Delete a user.                             |

---
## Folder Structure

```text
.
├── app/
│   ├── __pycache__/         # Compiled python files
│   └── main.py              # Application entry point and logic
├── img/                     # Folder containing the project screenshot
├── .gitattributes
├── .gitignore
├── LICENSE
├── test.db                  # SQLite Database (Auto-generated)
├── README.md
└── requirements.txt
```

---
## Installation
### 1. Clone the repository
```bash
https://github.com/HaiqalAly/Learn-CRUD-FAST-API
```
### 2. Create a Virtual Environtment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
uvicorn app.main:app --reload
```

### 5. Access the API
- API Root: http://127.0.0.1:8000
- Interactive Docs (Swagger UI): http://127.0.0.1:8000/docs

### 6. Register and Login
- To gain access to all endpoint you need to register (/register) and login (/token).
- Username is the email you entered and password is your password.
- Copy the access token and click Authorize.
- Enter username and password again then paste the token to client_secret

---
## License
This project is licensed under the MIT License.  
You are free to use, modify, and distribute this project for learning or development purposes.