from sqlmodel import Session
from src.exceptions import APIException
from src.repositories.user import UserRepository
from src.services.security import SecurityService


class AuthenticationService:
    def __init__(self):
        self._repository = UserRepository()
        self._security_service = SecurityService()

    def token(self, session: Session, email: str, password: str):
        user = self._repository.get_by_email(session, email)

        if not user:
            raise APIException("Invalid credentials", status_code=401)

        if not self._security_service.check_password(password, user.password):
            raise APIException("Invalid credentials", status_code=401)

        if not user.is_active:
            raise APIException("Invalid credentials", status_code=401)

        return self.generate_tokens(user.id)

    def validate(self, session: Session, headers: dict):
        try:
            authorization = headers.get("authorization")

            if not authorization:
                raise APIException("Invalid token", status_code=401)

            type, token = authorization.split()
            if type != "Bearer" or not token:
                raise APIException("Invalid token", status_code=401)

            data = self._security_service.decode_token(token, "access")
            user = self._repository.get_by_id(session, data["sub"])
            return user
        except Exception:
            raise APIException("Invalid token", status_code=401)

    def refresh(self, session: Session, refresh: str):
        try:
            decoded = self._security_service.decode_token(refresh, "refresh")
            user_id = int(decoded.get("sub"))
        except Exception:
            raise APIException("Invalid token", status_code=401)

        user = self._repository.get_by_id(session, user_id)
        if not user:
            raise APIException("Invalid token", status_code=401)

        return self.generate_tokens(user.id, generate_refresh=False)

    def register(self, session: Session, email: str, password: str, name: str):
        exists = self._repository.get_by_email(session, email)
        if exists:
            raise APIException("User already exists", status_code=400)

        hashed_password = self._security_service.hash_password(password)
        instance = self._repository.create(session, email, hashed_password, name)
        return self.generate_tokens(instance.id)

    def generate_tokens(self, user_id: int, generate_refresh: bool = True):
        access = self._security_service.create_token(user_id, "access")
        if not generate_refresh:
            return {"access": access, "type": "bearer"}

        refresh = self._security_service.create_token(user_id, "refresh")
        return {"access": access, "refresh": refresh, "type": "bearer"}
