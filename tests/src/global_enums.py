from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Recesived status code is not equal to expected."
    VALIDATION_FAILED = "Validation failed"
    HEADER_CONTENT_TYPE_NOT_JSON = "'content-type' is not JSON."


class HeaderContentType(Enum):
    JSON = 'application/json'
    TEXT = 'text/html'