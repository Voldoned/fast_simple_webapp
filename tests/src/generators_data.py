import faker

fake = faker.Faker()

users_data = [
    {
        "email": fake.unique.email(),
        "username": fake.unique.name(),
        "password": fake.unique.password(),
    }
    for _ in range(99)
]

articles_data = [
    {
        "title": fake.unique.text(),
        "text": fake.unique.text(),
        "annotation": fake.unique.text(),
    }
    for _ in range(99)
]

bad_users_data = [
    {
        "email": fake.unique.random_int(),
        "username": fake.unique.name(),
        "password": fake.unique.password(),
    }
    for _ in range(90)
]

bad_articles_data = [
    {
        "title": fake.unique.random_int(),
        "text": fake.unique.text(),
        "annotation": fake.unique.text(),
    }
    for _ in range(90)
]
