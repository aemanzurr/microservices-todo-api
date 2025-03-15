from fastapi import APIRouter, Request, Response
from src.database import SessionDep
from src.schemas.authentication import (
    RegisterRequestSchema,
    TokenRefreshRequestSchema,
    TokenRequestSchema,
    TokenResponseSchema,
)
from src.services.authentication import AuthenticationService

router = APIRouter(tags=["authentication"])
service = AuthenticationService()


@router.post("/login", response_model=TokenResponseSchema)
def token(data: TokenRequestSchema, session: SessionDep):
    tokens = service.token(session, data.email, data.password)
    return TokenResponseSchema(**tokens)


@router.post("/refresh", response_model=TokenResponseSchema)
def refresh(data: TokenRefreshRequestSchema, session: SessionDep):
    tokens = service.refresh(session, data.refresh)
    return TokenResponseSchema(**tokens)


@router.post("/validate")
def validate(request: Request, response: Response, session: SessionDep):
    user = service.validate(session, request.headers)
    response.headers["x-user-id"] = str(user.id)
    response.headers["x-user-email"] = user.email
    return {"detail": "ok"}


@router.post("/register", response_model=TokenResponseSchema)
def register(data: RegisterRequestSchema, session: SessionDep):
    tokens = service.register(session, data.email, data.password, data.name)
    return TokenResponseSchema(**tokens)
