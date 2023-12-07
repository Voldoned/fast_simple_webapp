# FastAPI + PostgreSQL + NginX + Redis + PyTest + Locust

## Variables in `.env`

Create file `.env` in work (this level) directory for run application with variables:
- `DB_HOST` -- addres to DB
- `DB_PORT` -- port to DB
- `DB_USER` -- name user DB
- `DB_PASSWORD` -- User's password DB
- `DB_NAME` -- name of DB
- `REDIS_HOST` -- addres to redis DB
- `REDIS_PORT` -- port to redis DB

## Run
In terminal
```bash
sudo docker compose build && sudo docker compose up
```
or
```bash
sudo docker compose build && sudo docker compose up -d
```

## API

Address app: `http://0.0.0.0:8080`

Swagger documentation: `http://0.0.0.0:8080/docs`
