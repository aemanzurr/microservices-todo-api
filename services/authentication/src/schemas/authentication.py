from pydantic import BaseModel


class TokenRequestSchema(BaseModel):
    email: str
    password: str


class TokenRefreshRequestSchema(BaseModel):
    refresh: str


class RegisterRequestSchema(BaseModel):
    name: str
    email: str
    password: str


class TokenResponseSchema(BaseModel):
    access: str
    refresh: str | None = None
    type: str
