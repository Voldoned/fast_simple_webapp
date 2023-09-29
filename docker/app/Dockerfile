FROM python:latest

WORKDIR /mnt/fastapp

COPY .env .

COPY ./docker/app/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./fastapp .
