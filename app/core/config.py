from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str = "postgres"
    POSTGRES_PORT: int = 5432

    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str 
    JWT_EXPIRE_MINUTES: int 

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

settings = Settings()