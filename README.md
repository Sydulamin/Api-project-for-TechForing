
# Project Management API

This project provides a **RESTful API** for a project management tool. It allows users to manage projects, tasks, and comments, with JWT-based authentication. The backend is built using **Django** and **Django REST Framework**, with **JWT** authentication and **drf-yasg** for Swagger documentation.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set up the Virtual Environment](#2-set-up-the-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Set up the Database](#4-set-up-the-database)
  - [5. Run the Development Server](#5-run-the-development-server)
- [Usage](#usage)
  - [1. Access the API](#1-access-the-api)
  - [2. Authentication](#2-authentication)
  - [3. API Endpoints](#3-api-endpoints)
- [Testing](#testing)
- [Swagger Documentation](#swagger-documentation)
- [Contributing](#contributing)
- [License](#license)
- [Notes](#notes)

---

## Features

- **User Management**: Create, update, and delete user profiles.
- **JWT Authentication**: Secure login for users with token-based authentication (admin-only for access).
- **Projects**: Create, list, update, and delete projects.
- **Tasks**: Add, update, list, and delete tasks within a project.
- **Comments**: Add, update, list, and delete comments on tasks.
- **Admin Access**: Only admins can create JWT tokens.

---

## Technologies Used

- **Django**: Web framework for the backend.
- **Django REST Framework**: To create the API endpoints.
- **JWT Authentication**: Token-based authentication with **djangorestframework-simplejwt**.
- **drf-yasg**: For generating Swagger UI documentation.
- **SQLite**: Database for development (can be switched to other databases like PostgreSQL).
- **Python 3.13** (or higher recommended).

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/project-management-api.git
cd project-management-api
```

### 2. Set up the Virtual Environment

Make sure you have `python3` and `pip` installed. Then, create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scriptsctivate     # For Windows
```

### 3. Install Dependencies

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

This will install all the necessary packages, including Django, Django REST Framework, JWT, and drf-yasg.

### 4. Set up the Database

Apply the migrations to create the necessary database tables:

```bash
python manage.py migrate
```

### 5. Run the Development Server

Run the server to start the application:

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

---

## Usage

### 1. Access the API

Once the server is running, you can access the API through the following endpoints:

- **Users**: `/api/users/`
- **Projects**: `/api/projects/`
- **Tasks**: `/api/projects/{project_id}/tasks/`
- **Comments**: `/api/tasks/{task_id}/comments/`

### 2. Authentication

- **Admin Login**: Use the `/api/token/` endpoint to log in as an admin and obtain a JWT token.

  - **Request**:
    ```json
    {
      "username": "admin_user",
      "password": "admin_password"
    }
    ```

  - **Response**:
    ```json
    {
      "access": "jwt_access_token",
      "refresh": "jwt_refresh_token"
    }
    ```

- **Access Protected Endpoints**: Once authenticated, you need to include the JWT access token in the `Authorization` header for all protected routes. Example:
  ```
  Authorization: Bearer jwt_access_token
  ```

### 3. API Endpoints

Here are the available API endpoints:

#### Users Endpoints

- `GET /api/users/`: List all users.
- `POST /api/users/`: Create a new user.
- `GET /api/users/{id}/`: Retrieve user details.
- `PUT /api/users/{id}/`: Update user details.
- `DELETE /api/users/{id}/`: Delete a user.

#### Projects Endpoints

- `GET /api/projects/`: List all projects.
- `POST /api/projects/`: Create a new project.
- `GET /api/projects/{id}/`: Retrieve a project’s details.
- `PUT /api/projects/{id}/`: Update a project.
- `DELETE /api/projects/{id}/`: Delete a project.

#### Tasks Endpoints

- `GET /api/projects/{project_id}/tasks/`: List tasks within a project.
- `POST /api/projects/{project_id}/tasks/`: Create a new task.
- `GET /api/tasks/{id}/`: Retrieve task details.
- `PUT /api/tasks/{id}/`: Update a task.
- `DELETE /api/tasks/{id}/`: Delete a task.

#### Comments Endpoints

- `GET /api/tasks/{task_id}/comments/`: List comments for a task.
- `POST /api/tasks/{task_id}/comments/`: Add a comment to a task.
- `GET /api/comments/{id}/`: Retrieve a comment.
- `PUT /api/comments/{id}/`: Update a comment.
- `DELETE /api/comments/{id}/`: Delete a comment.

---

## Testing

To test the API endpoints, you can use tools like **Postman** or **cURL**. Alternatively, once the server is running, you can test the endpoints directly in the **Swagger UI** (described below).

---

## Swagger Documentation

The project uses **drf-yasg** to generate an interactive Swagger UI for API documentation.

- Visit `http://127.0.0.1:8000/swagger/` to view and interact with the API.
- You can see the available endpoints, parameters, and responses.
- You can test the API directly from the Swagger UI by logging in with the admin token.

---

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Run tests (if applicable).
5. Submit a pull request with a clear description of your changes.

---

## License

This project is licensed under the MIT License. See the **[LICENSE](LICENSE)** file for details.

---

## Notes

- **Environment variables**: You may want to configure a `.env` file for sensitive data such as `SECRET_KEY` and database credentials.
- Make sure the API runs smoothly and all endpoints are tested thoroughly before deploying it to production.

---
