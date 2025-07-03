from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class IncidentBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str

class IncidentCreate(IncidentBase):
    pass

class IncidentRead(IncidentBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True  # For SQLAlchemy ORM mode in Pydantic v2

class IncidentResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    timestamp: datetime

    class Config:
        from_attributes = True
	orm_mode = True
