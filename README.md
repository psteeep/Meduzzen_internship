# Backend with FastAPI

## Setup

---
* For installing required packages, execute the following command in terminal:
    ``pip install -r requirements.txt``
* For run:
    
    ``uvicorn app.main:app --reload``
* For run tests:

    ``python -m tests``

## Dockerfile

---
* For build container:
    ``sudo docker build -t myimage``
* For run app and tests:
    ``sudo docker run  --name mycontainer -p 8000:8000 myimage``

## Migrations

---
* ``alembic revision --autogenerate -m "migration name"``
* ``alembic upgrade head``