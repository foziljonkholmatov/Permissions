from rest_framework.exceptions import APIException


class AppException(APIException):
    status_code = 400
    default_detail = "Unexpected error occurred."
    default_code = 'app_error'

    def __init__(self, detail=None, status_code=None):
        if detail is not None:
            self.detail = {'error': detail}
        if status_code is not None:
            self.status_code = status_code
            