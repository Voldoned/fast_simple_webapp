from pydantic import BaseModel

from ..base_classes.base_response import BaseResponse


def asserting_response(response, status_code: int, validate_schema: BaseModel = None):
    try:
        response_obj = BaseResponse(response)

        response_obj.assert_status_code(status_code)

        response_obj.assert_has_response_json()
        if validate_schema:
            response_obj.validate_json(validate_schema)

        return response_obj
    except Exception as ex:
        raise ex
