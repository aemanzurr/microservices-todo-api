from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # INFORMATION
    SERVICE_NAME: str = "authentication"
    SERVICE_DESCRIPTION: str = "authentication service"
    SERVICE_VERSION: str = "0.0.1"

    # SECURITY
    DEBUG: bool = True
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ACCESS_TOKEN_SECRET_KEY: str = "access-secret-key"
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    REFRESH_TOKEN_SECRET_KEY: str = "refresh-secret-key"
    ALGORITHM: str = "HS256"

    # DATABASE
    DATABASE_URL: str = "mysql://root:admin-password@db:3306/authentication"


settings = Settings()
