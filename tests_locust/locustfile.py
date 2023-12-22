import random
from datetime import datetime
import faker

from locust import HttpUser, task, constant_throughput

from src.pydantic_schemas import UsersSchema, CreateUserResponseSchema
from src.utils.request_context import request_locust
from src.utils.testing_response import asserting_response

HEADERS = {
    "Accept": "text/html,"
    "application/json,"
    "application/xhtml+xml,"
    "application/xml;q=0.9,"
    "image/avif,"
    "image/webp,"
    "image/apng,*/*;q=0.8,"
    "application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "localhost:8000",
    "Sec-Ch-Ua": '"Not.A/Brand";v="8", '
    '"Chromium";v="114", '
    '"Google Chrome";v="114"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/114.0.0.0 "
    "Safari/537.36",
}

fake = faker.Faker()


class TestLocust(HttpUser):
    # Пользователь будет отправлять 1 запрос в секунду
    wait_time = constant_throughput(0.5)
    count_users: int = 1

    @task(1)
    def get_users_request(self):
        transaction = self.get_users_request.__name__

        response_create = request_locust(
            self,
            method="POST",
            url="/users/add",
            headers=HEADERS,
            json={
                "email": fake.unique.email(),
                "username": fake.unique.name(),
                "password": fake.unique.password(),
                "registered_at": datetime.now().isoformat(),
            },
            catch_response=True,
            name=f"{transaction}_1",
        )
        try:
            response_count_obj = asserting_response(
                response=response_create,
                status_code=200,
                validate_schema=CreateUserResponseSchema,
            )
            self.count_users = response_count_obj.response_json["count_users"]
        except Exception as ex:
            response_create.failure(ex)

        response_get = request_locust(
            self,
            method="GET",
            url="/users/",
            headers=HEADERS,
            catch_response=True,
            name=f"{transaction}_2",
        )
        try:
            asserting_response(
                response=response_create,
                status_code=200,
                validate_schema=UsersSchema,
            )
        except Exception as ex:
            response_get.failure(ex)

    @task(1)
    def get_count_users_request(self):
        transaction = self.get_count_users_request.__name__

        # Создаем экземпляр класса BaseResponse и проверяем корректность
        # ответа сервера
        response_get = request_locust(
            self,
            method="GET",
            url="/users/count_users",
            headers=HEADERS,
            catch_response=True,
            name=transaction,
        )
        try:
            asserting_response(response=response_get, status_code=200)
        except Exception as ex:
            response_get.failure(ex)

    @task(1)
    def update_user_request(self):
        transaction = self.update_user_request.__name__

        update_user_data = {
            "email": fake.unique.email(),
            "username": fake.unique.name(),
            "password": fake.unique.password(),
            "id": random.randint(1, int((self.count_users - self.count_users % 2) / 2)),
        }

        response_put = request_locust(
            self,
            method="PUT",
            url="/users/update",
            headers=HEADERS,
            json=update_user_data,
            catch_response=True,
            name=f"{transaction}",
        )

        def __check_update_data(response):
            try:
                response_update_obj = asserting_response(
                    response=response, status_code=200
                )

                updated_data = response_update_obj.response_json["data"]

                assert (
                    updated_data == update_user_data
                ), f"Updating error:\n{update_user_data=}\n{updated_data=}"
            except Exception as ex:
                response.failure(ex)

        __check_update_data(response_put)
