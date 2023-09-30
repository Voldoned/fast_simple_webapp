import pytest

from src.base_classes.base_response import BaseResponse
from src.base_classes.api_client import APIClient
from src.pydantic_schemas import UserSchema, CreateUserResponse, ErrorMessage
from src.generators_data import users_data, bad_users_data


class TestHTTP:
    URL_AND_CODE_FOR_GET_USERS_REQUESTS = [
        ("/get_data/users", 200),
        ("/get_data/users/first/10", 200),
        ("/get_data/users/first/0", 406),
    ]

    URL_AND_CODE_POST_REQUESTS = [
        ("/get_data/user/add", users_data, 200),
        ("/get_data/user/add", bad_users_data, 422),
    ]

    @pytest.mark.parametrize('url_path, users_data, status_code',
                             URL_AND_CODE_POST_REQUESTS)
    def test_status_code_post_request(self, domen: str,
                                      headers_for_requests: dict,
                                      url_path: str, users_data: list[dict],
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
                response_obj.assert_has_response_json()
                response_obj.validate_json(CreateUserResponse)

    @pytest.mark.parametrize("url_path, status_code",
                             URL_AND_CODE_FOR_GET_USERS_REQUESTS)
    def test_status_code_get_request(self, domen, headers_for_requests,
                                     url_path: str, status_code: int):
        response = APIClient(domen).get(
            path=url_path,
            headers=headers_for_requests
        )

        response_obj: BaseResponse = BaseResponse(response)

        response_obj.assert_status_code(status_code)
        response_obj.assert_has_response_json()

        if status_code == 200:
            response_obj.validate_json(UserSchema)
        else:
            response_obj.validate_json(ErrorMessage)
