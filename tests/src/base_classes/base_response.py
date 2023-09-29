from pydantic import BaseModel
from requests import Response

from src.enums.global_enums import GlobalErrorMessages as GEM, \
    HeaderContentType as HCT


class BaseResponse:

    def __init__(self, response: Response):
        self.response = response
        self.response_status_code = response.status_code
        self.response_headers = dict(response.headers)
        self.request_method = response.request.method
        self.request_headers = dict(response.request.headers)
        self.response_json = response.json()

    def __str__(self):
        print(self.response_headers)
        print(self.response_json)
        output = f"\nStatus code: {self.response_status_code}" \
                 f" Request URL: {self.response.url}"

        if self.response_json:
            return output + f" Request JSON: {self.response_json}"
        else:
            return output

    # def get_request_headers(self) -> dict:
    #     return self.request_headers
    #
    # def get_response_headers(self) -> dict:
    #     return self.response_headers

    def assert_status_code(self, status_code):
        if isinstance(status_code, (list, tuple)):
            assert self.response_status_code in status_code, \
                GEM.WRONG_STATUS_CODE.value
        else:
            assert self.response_status_code == status_code, \
                GEM.WRONG_STATUS_CODE.value + (f" Status code: "
                                               f"{self.response_status_code}")

    def assert_has_response_json(self):
        assert self.response_json, GEM.HEADER_CONTENT_TYPE_NOT_JSON.value + \
            (f" Header 'content-type': {self.response_headers['content-type']}.")

        assert self.response_json, f"JSON: {self.response_json}."

    def validate_json(self, schema: type[BaseModel]):
        if self.response_json:
            if isinstance(self.response_json, (list, tuple)):
                for i in self.response_json:
                    schema.model_validate(i)
            else:
                schema.model_validate(self.response_json)

            return self.response_json
        else:
            return None
