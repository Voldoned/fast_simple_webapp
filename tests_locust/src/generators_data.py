import faker
from datetime import datetime

fake = faker.Faker()

users_data = [
    {
        "email": fake.unique.email(),
        "username": fake.unique.name(),
        "password": fake.unique.password(),
        "registered_at": datetime.now().isoformat()
    }
    for _ in range(9)
]

articles_data = [
    {
        "title": fake.unique.text(),
        "text": fake.unique.text(),
        "annotation": fake.unique.text(),
        "published_at": datetime.now().isoformat()
    }
    for _ in range(9)
]

bad_users_data = [
    {
        "email": fake.unique.random_int(),
        "username": fake.unique.name(),
        "password": fake.unique.password(),
        "registered_at": datetime.now().isoformat()
    }
    for _ in range(9)
]

bad_articles_data = [
    {
        "title": fake.unique.random_int(),
        "text": fake.unique.text(),
        "annotation": fake.unique.text(),
        "published_at": datetime.now().isoformat()
    }
    for _ in range(9)
]
