# FastAPI + PostgreSQL + NginX

## API

out host app: 0.0.0.0

out port app: 8000

get:
- `/get_data_users` -- list of users (ID, name, password, email, registered at)
- `/get_data/user/{id}` -- return user with ID = {id}
- `/get_data/user/first/{count}` -- return first {count} users

post:
- `/get_data/user/add` -- create new user

## Variables in `.env`

Create file `.env` in work directory for run application with variables:
- `DB_HOST` -- addres to DB
- `DB_PORT` -- port to DB
- `DB_USER` -- name user DB
- `DB_PASSWORD` -- User's password DB
- `DB_NAME` -- name of DB


## Run
In terminal
```bash
sudo docker-compose build && sudo docker-compose up
```
or
```bash
sudo docker-compose build && sudo docker-compose up -d
```