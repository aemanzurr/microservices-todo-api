from fastapi import APIRouter, Request, responses
from src.database import SessionDep
from src.schemas.task import TaskCreateSchema, TaskPublic
from src.services.task import TaskService

router = APIRouter(tags=["task"])
service = TaskService()


@router.post("/")
def create(request: Request, data: TaskCreateSchema, session: SessionDep):
    task = service.create(session, request.state.user_id, data.title, data.description)
    return TaskPublic(**task.model_dump())


@router.get("/")
def get_all(request: Request, session: SessionDep):
    tasks = service.get_all(session, request.state.user_id)
    return [TaskPublic(**task.model_dump()) for task in tasks]


@router.get("/{task_id}")
def get_one(request: Request, task_id: int, session: SessionDep):
    task = service.get_one(session, request.state.user_id, task_id)
    if not task:
        return responses.JSONResponse(status_code=404, content={"detail": "Task not found"})

    return TaskPublic(**task.model_dump())


@router.put("/{task_id}")
def update(request: Request, task_id: int, data: TaskCreateSchema, session: SessionDep):
    task = service.update(session, request.state.user_id, task_id, data.title, data.description)
    if not task:
        return responses.JSONResponse(status_code=404, content={"detail": "Task not found"})

    return TaskPublic(**task.model_dump())


@router.put("/{task_id}/complete")
def complete(request: Request, task_id: int, session: SessionDep):
    task = service.complete(session, request.state.user_id, task_id)
    if not task:
        return responses.JSONResponse(status_code=404, content={"detail": "Task not found"})

    return TaskPublic(**task.model_dump())


@router.delete("/{task_id}")
def delete(request: Request, task_id: int, session: SessionDep):
    task = service.delete(session, request.state.user_id, task_id)
    if not task:
        return responses.JSONResponse(status_code=404, content={"detail": "Task not found"})

    return TaskPublic(**task.model_dump())
