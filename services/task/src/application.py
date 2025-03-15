from fastapi import FastAPI
from fastapi.requests import Request

from .database import create_db_and_tables
from .routes.task import router as task_router
from .settings import settings

# APPLICATION
application = FastAPI(
    title=settings.SERVICE_NAME,
    description=settings.SERVICE_DESCRIPTION,
    version=settings.SERVICE_VERSION,
    debug=settings.DEBUG,
    docs_url="/docs" if settings.DEBUG else None,
)


# EVENTS
application.add_event_handler("startup", create_db_and_tables)


# MIDDLEWARE'S
@application.middleware("http")
async def authentication(request: Request, call_next):
    user_id = request.headers.get("x-user-id")
    user_email = request.headers.get("x-user-email")

    request.state.user_id = user_id
    request.state.user_email = user_email

    response = await call_next(request)
    return response


# ROUTES
application.include_router(task_router)
