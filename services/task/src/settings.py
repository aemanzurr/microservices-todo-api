from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # INFORMATION
    SERVICE_NAME: str = "task"
    SERVICE_DESCRIPTION: str = "wharehouse service"
    SERVICE_VERSION: str = "0.0.1"

    # SECURITY
    DEBUG: bool = True

    # DATABASE
    DATABASE_URL: str = "mysql://root:admin-password@db:3306/task"


settings = Settings()
