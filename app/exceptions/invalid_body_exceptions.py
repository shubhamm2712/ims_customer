from fastapi import HTTPException, status

class InvalidBodyException(HTTPException):
    def __init__(self, detail: str, **kwargs):
        super().__init__(status.HTTP_400_BAD_REQUEST, detail=detail)