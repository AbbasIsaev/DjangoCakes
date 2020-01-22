UNKNOWN_ERROR = 'Неизвестная ошибка'


class ExceptionHandler(Exception):
    def __init__(self, err):  # real signature unknown
        self.error = err
        pass

    def __str__(self):
        if self.error.strerror is not None:
            return self.error.strerror

        response = getattr(self.error, 'response', None)
        if response is not None:
            return '{code} {reason}'.format(
                code=self.error.response.status_code,
                reason=self.error.response.reason)
        return UNKNOWN_ERROR
