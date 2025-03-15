from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class UserModel(SQLModel, table=True):
    __tablename__ = "users"

    id: int = Field(primary_key=True)
    name: str
    email: str = Field(index=True, unique=True)
    password: str
    is_active: bool = True
    created_at: datetime = Field(default=datetime.now(timezone.utc))
    updated_at: datetime = Field(default=datetime.now(timezone.utc))
