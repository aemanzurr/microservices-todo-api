from sqlmodel import Session, select
from src.models.task import TaskModel


class TaskRepository:
    def __init__(self):
        self.model = TaskModel

    def get_one_by_user_id(self, session: Session, user_id: int, id: int) -> TaskModel:
        statement = select(self.model).where(self.model.user_id == user_id).where(self.model.id == id)
        return session.exec(statement).first()

    def get_all_by_user_id(self, session: Session, user_id: int) -> list[TaskModel]:
        statement = select(self.model).where(self.model.user_id == user_id)
        return session.exec(statement).all()

    def create(self, session: Session, user_id: int, title: str, description: str) -> TaskModel:
        task = self.model(user_id=user_id, title=title, description=description)
        session.add(task)
        session.commit()
        session.refresh(task)
        return task

    def update(self, session: Session, id: int, title: str, description: str, completed: bool, completed_at=None) -> TaskModel:
        task = session.get(self.model, id)
        task.title = title
        task.description = description
        task.completed = completed
        task.completed_at = completed_at
        session.add(task)
        session.commit()
        session.refresh(task)
        return task

    def delete(self, session: Session, id: int) -> None:
        task = session.get(self.model, id)
        session.delete(task)
        session.commit()
