from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from datetime import datetime

router = APIRouter(prefix="/incidents", tags=["incidents"])

class Incident(BaseModel):
    id: int
    title: str
    status: str
    timestamp: datetime

incident_store: List[Incident] = []

@router.get("/", response_model=List[Incident])
def get_incidents():
    return incident_store

@router.post("/", response_model=Incident)
def create_incident(incident: Incident):
    incident_store.append(incident)
    return incident
