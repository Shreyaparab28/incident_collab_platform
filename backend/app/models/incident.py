from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base
from datetime import datetime

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, default="open")
    severity = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
