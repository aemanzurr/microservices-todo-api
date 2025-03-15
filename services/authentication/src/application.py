from fastapi import FastAPI

from .database import create_db_and_tables
from .routes.authentication import router as authentication_router
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


# ROUTES
application.include_router(authentication_router)
