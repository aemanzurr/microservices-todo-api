from sqlmodel import Session, select
from src.models.user import UserModel


class UserRepository:
    def __init__(self):
        self.model = UserModel

    def get_by_email(self, session: Session, email: str) -> UserModel | None:
        statement = select(self.model).where(self.model.email == email)
        return session.exec(statement).first()

    def get_by_id(self, session: Session, id: int) -> UserModel | None:
        return session.get(self.model, id)

    def get_all(self, session: Session) -> list[UserModel]:
        return session.exec(select(self.model)).all()

    def create(self, session: Session, email: str, password: str, name: str) -> UserModel:
        user = self.model(email=email, password=password, name=name)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def delete(self, session: Session, id: int) -> None:
        user = session.get(self.model, id)
        session.delete(user)
        session.commit()
