FROM python:latest

WORKDIR /mnt/fastapp

COPY ./docker/app/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./fastapp .

RUN alembic init migrate
COPY /docker/app/env.py ./migrate/env.py

COPY .env .
