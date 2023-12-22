import random
import pytest

from src.base_classes.base_response import BaseResponse
from src.base_classes.api_client import APIClient
from src.pydantic_schemas import (
    UsersSchema, CreateUserResponse,
    ArticlesSchema, CreateArticleResponseSchema,
    ErrorMessageSchema
)
from src.generators_data import (
    users_data, bad_users_data,
    articles_data, bad_articles_data
)


class TestUsersHTTP:
    URL_AND_CODE_FOR_GET_USERS_REQUESTS = [
        ("/users/", UsersSchema, 200),
        ("/users/head/2", UsersSchema, 200),
        ("/users/head/0", ErrorMessageSchema, 406),
    ]

    URL_AND_CODE_POST_REQUESTS = [
        ("/users/add", users_data, CreateUserResponse, 200),
        ("/users/add", bad_users_data, ErrorMessageSchema, 422),
    ]

    @pytest.mark.parametrize('url_path, users_data, schema, status_code',
                             URL_AND_CODE_POST_REQUESTS)
    def test_status_code_post_request(self, domen: str,
                                      headers_for_requests: dict,
                                      url_path: str, users_data: list[dict],
                                      schema,
                                      status_code: int):
        for user_data in users_data:
            response = APIClient(domen).post(
                path=url_path,
                headers=headers_for_requests,
                json=user_data
            )

            response_obj: BaseResponse = BaseResponse(response)

            response_obj.assert_status_code(status_code)
            if status_code == 200:
                response_obj.validate_json(schema)
            else:
                response_obj.validate_json(schema)

    @pytest.mark.parametrize("url_path, schema, status_code",
                             URL_AND_CODE_FOR_GET_USERS_REQUESTS)
    def test_status_code_get_request(self, domen, headers_for_requests,
                                     url_path: str, schema, status_code: int):
        response = APIClient(domen).get(
            path=url_path,
            headers=headers_for_requests
        )

        response_obj: BaseResponse = BaseResponse(response)

        response_obj.assert_status_code(status_code)
        response_obj.assert_has_response_json()

        if status_code == 200:
            response_obj.validate_json(schema)
        else:
            response_obj.validate_json(schema)


class TestArticlesHTTP:
    URL_AND_CODE_FOR_GET_USERS_REQUESTS = [
        ("/articles/", ArticlesSchema, 200),
        ("/articles/head/2", ArticlesSchema, 200),
        ("/articles/head/0", ErrorMessageSchema, 406),
    ]

    URL_AND_CODE_POST_REQUESTS = [
        ("/articles/add", articles_data, CreateArticleResponseSchema, 200),
        ("/articles/add", bad_articles_data, ErrorMessageSchema, 422),
    ]

    @pytest.mark.parametrize('url_path, users_data, schema, status_code',
                             URL_AND_CODE_POST_REQUESTS)
    def test_status_code_post_request(self, domen: str,
                                      headers_for_requests: dict,
                                      url_path: str, users_data: list[dict],
                                      schema,
                                      status_code: int):
        count_users = APIClient(domen).get(
            path="/users/count_users",
            headers=headers_for_requests,
        ).json()["count_users"]
        users_id = [random.randrange(1, count_users, 1) for _ in range(800)]
        for user_data in users_data:
            user_id = {
                "user_id": random.choice(users_id)
            }

            response = APIClient(domen).post(
                path=url_path,
                headers=headers_for_requests,
                json=dict(**user_data, **user_id)
            )

            response_obj: BaseResponse = BaseResponse(response)

            response_obj.assert_status_code(status_code)
            if status_code == 200:
                response_obj.validate_json(schema)
            else:
                response_obj.validate_json(schema)

    @pytest.mark.parametrize("url_path, schema, status_code",
                             URL_AND_CODE_FOR_GET_USERS_REQUESTS)
    def test_status_code_get_request(self, domen, headers_for_requests,
                                     url_path: str, schema, status_code: int):
        response = APIClient(domen).get(
            path=url_path,
            headers=headers_for_requests
        )

        response_obj: BaseResponse = BaseResponse(response)

        response_obj.assert_status_code(status_code)
        response_obj.assert_has_response_json()

        if status_code == 200:
            response_obj.validate_json(schema)
        else:
            response_obj.validate_json(schema)
