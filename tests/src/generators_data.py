import faker
from datetime import datetime

fake = faker.Faker()

users_data = [
    {
        "id": fake.unique.random_int(),
        "email": fake.unique.email(),
        "username": fake.unique.name(),
        "password": fake.unique.password(),
        "registered_at": datetime.now().isoformat()
    }
    for _ in range(900)
]

bad_users_data = [
    {
        "id": fake.unique.text(),
        "email": fake.unique.email(),
        "username": fake.unique.name(),
        "password": fake.unique.password(),
        "registered_at": datetime.now().isoformat()
    }
    for _ in range(90)
]
