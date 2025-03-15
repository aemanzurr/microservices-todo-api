from datetime import datetime, timedelta, timezone
from typing import Any, Literal, Union

from jose import jwt
from passlib.context import CryptContext
from src.settings import settings


class SecurityService:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str):
        return self.pwd_context.hash(password)

    def check_password(self, password: str, hashed_password: str):
        return self.pwd_context.verify(password, hashed_password)

    def create_token(self, subject: Union[str, Any], token_type: Literal["access", "refresh"]) -> str:
        now = datetime.now(timezone.utc)
        secret_key = settings.ACCESS_TOKEN_SECRET_KEY if token_type == "access" else settings.REFRESH_TOKEN_SECRET_KEY
        expires = settings.ACCESS_TOKEN_EXPIRE_MINUTES if token_type == "access" else settings.REFRESH_TOKEN_EXPIRE_MINUTES
        expires_delta = now + timedelta(minutes=expires)
        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, secret_key, settings.ALGORITHM)
        return encoded_jwt

    def decode_token(self, token: str, token_type: Literal["access", "refresh"]) -> dict:
        secret_key = settings.ACCESS_TOKEN_SECRET_KEY if token_type == "access" else settings.REFRESH_TOKEN_SECRET_KEY
        return jwt.decode(token, secret_key, algorithms=[settings.ALGORITHM])
