import json
from typing import Dict


class APIError(Exception):
    def __init__(self, message: str, code: str, extra: Dict) -> None:
        self.message = message
        self.code = code
        self.extra = extra

    def __str__(self) -> str:
        return json.dumps(
            {"message": self.message, "code": self.code, "extra": self.extra}
        )


class Unauthenticated(APIError):
    pass


class NotFound(APIError):
    pass


class BadRequest(APIError):
    pass
