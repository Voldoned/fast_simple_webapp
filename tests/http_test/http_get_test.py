import pytest

from src.base_classes.base_response import BaseResponse
from src.base_classes.api_client import APIClient
from src.pydantic_schema import UserSchema

from src.pydantic_schema import CreateUserResponse


class TestHTTP:
    URLS_FOR_GET_REQUESTS = [
        "/get_data/users",
        "/get_data/user/0",
        "/get_data/users/first/1",
    ]

    URLS_FOR_POST_REQUESTS = [
        "/get_data/user/add"
    ]

    @pytest.mark.parametrize('url_path', URLS_FOR_POST_REQUESTS)
    def test_status_code_post_request(self, domen, headers_for_requests,
                                      url_path):
        data = {
            "id": 0,
            "email": "string",
            "username": "string",
            "password": "string",
            "registered_at": "2023-09-27T15:33:57.764"
        }

        response = APIClient(domen).post(
            path=url_path,
            headers=headers_for_requests,
            json=data,
        )

        response_obj: BaseResponse = BaseResponse(response)

        response_obj.assert_status_code(200)
        response_obj.assert_has_response_json()
        response_obj.validate_json(CreateUserResponse)

    @pytest.mark.parametrize('url_path', URLS_FOR_GET_REQUESTS)
    def test_status_code_get_request(self, domen, headers_for_requests,
                                     url_path):
        response = APIClient(domen).get(
            path=url_path,
            headers=headers_for_requests
        )

        response_obj: BaseResponse = BaseResponse(response)

        response_obj.assert_status_code(200)
        response_obj.assert_has_response_json()
        response_obj.validate_json(UserSchema)
