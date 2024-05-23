# FastAPI User Management Service

A backend FastAPI service designed to facilitate user management operations with ease. It serves as a lightweight CRM tool tailored for controlling users within your system. With built-in authentication features, it ensures secure access and data management, offering a seamless experience for both administrators.

## Features

- User management (CRUD operations)
- Authentication and Authorization
- Secure data handling
- Lightweight and efficient
- Easy to integrate with existing systems

## Quick Start

### Prerequisites

- Python 3.9+
- Docker (optional, for containerization)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To run the FastAPI application:

```bash
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

### Running Tests

To run the tests:

```bash
python -m tests
```

## Docker

### Building the Docker Container

To build the Docker container:

```bash
sudo docker build -t myimage .
```

### Running the Docker Container

To run the application and expose it on port 8000:

```bash
sudo docker run --name mycontainer -p 8000:8000 myimage
```

### Running Tests in Docker

Ensure your Dockerfile is configured to include test dependencies and scripts. Then you can run tests similarly to how you run the application.

## Database Migrations

### Alembic Migrations

To create a new migration:

```bash
alembic revision --autogenerate -m "migration name"
```

To apply the migrations:

```bash
alembic upgrade head
```
