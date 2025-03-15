from datetime import datetime

from pydantic import BaseModel


class TaskPublic(BaseModel):
    id: int
    title: str
    description: str
    created_at: str | datetime
    updated_at: str | datetime
    completed: bool
    completed_at: str | datetime | None


class TaskCreateSchema(BaseModel):
    title: str
    description: str
