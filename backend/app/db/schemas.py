from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class IncidentBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "Open"

class IncidentCreate(IncidentBase):
    pass

class IncidentResponse(IncidentBase):
    id: int
    created_at: datetime
    created_by: Optional[str]
    model_config = ConfigDict(from_attributes=True)
