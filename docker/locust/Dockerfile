FROM python:3.8

WORKDIR /mnt/locust

COPY /docker/locust/requirements.txt .
RUN pip install -r requirements.txt

COPY /tests_locust .
