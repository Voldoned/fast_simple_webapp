FROM python:3.8

WORKDIR /mnt/fastapp

COPY ./docker/app/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./fastapp .
COPY ./.env ./.env



