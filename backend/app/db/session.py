import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from contextlib import asynccontextmanager

# Use environment variables or defaults for clarity and flexibility
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@db:5432/incident_db")

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create sessionmaker for AsyncSession
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Declare base
Base = declarative_base()

# Dependency to get DB session for FastAPI routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
