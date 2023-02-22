FROM python:3.10

WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

COPY . /app

EXPOSE 8000


CMD python3 -m pytest; uvicorn app.main:app --host 0.0.0.0 --port 8000; python system_config.py
