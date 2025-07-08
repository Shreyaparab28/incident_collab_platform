import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from typing import AsyncGenerator

# Determine if running inside Docker
DOCKER_ENV = os.getenv("DOCKER_ENV", "false").lower() == "true"

if DOCKER_ENV:
    DATABASE_URL = "postgresql+asyncpg://postgres:postgres@db:5432/incident_db"
else:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/incident_db")

print(f"Using DATABASE_URL: {DATABASE_URL}")

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
