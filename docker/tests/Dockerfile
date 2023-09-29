FROM python:latest

COPY ./docker/tests/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./tests .

CMD ["pytest", "-v", "-s", "http_test"]