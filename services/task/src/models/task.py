from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class TaskModel(SQLModel, table=True):
    __tablename__ = "tasks"

    id: int = Field(default=None, primary_key=True)
    user_id: int
    title: str
    description: str
    created_at: datetime = Field(default=datetime.now(timezone.utc))
    updated_at: datetime = Field(default=datetime.now(timezone.utc))
    completed: bool = Field(default=False)
    completed_at: datetime = Field(default=None, nullable=True)
