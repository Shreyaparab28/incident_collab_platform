# backend/app/db/schemas.py
from pydantic import BaseModel

class IncidentBase(BaseModel):
    title: str
    description: str

class IncidentCreate(IncidentBase):
    pass

class Incident(IncidentBase):
    id: int

    class Config:
        orm_mode = True
