from pydantic import BaseModel, ConfigDict
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
    created_at: datetime

class IncidentResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    created_at: datetime

class Config:
        orm_mode = True