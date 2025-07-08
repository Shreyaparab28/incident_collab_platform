from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/incident_db"
    # your other configs...

    class Config:
        env_file = ".env"

settings = Settings()
