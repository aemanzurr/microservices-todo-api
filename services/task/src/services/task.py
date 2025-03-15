from datetime import datetime, timezone

from sqlmodel import Session
from src.repositories.task import TaskRepository


class TaskService:
    def __init__(self):
        self._repository = TaskRepository()

    def get_all(self, session: Session, user_id: int):
        return self._repository.get_all_by_user_id(session, user_id)

    def get_one(self, session: Session, user_id: int, task_id: int):
        return self._repository.get_one_by_user_id(session, user_id, task_id)

    def create(self, session: Session, user_id: int, title: str, description: str = ""):
        return self._repository.create(session, user_id, title, description)

    def delete(self, session: Session, user_id: int, task_id: int):
        task = self.get_one(session, user_id, task_id)
        if task:
            self._repository.delete(session, task_id)
            return task
        return None

    def update(self, session: Session, user_id: int, task_id: int, title: str, description: str):
        task = self.get_one(session, user_id, task_id)
        if task:
            return self._repository.update(session, task_id, title, description, task.completed)
        return None

    def complete(self, session: Session, user_id: int, task_id: int):
        completed = True
        now = datetime.now(timezone.utc)
        task = self.get_one(session, user_id, task_id)
        if task:
            if task.completed:
                completed = False
                now = None

            return self._repository.update(session, task_id, task.title, task.description, completed, now)
        return None
