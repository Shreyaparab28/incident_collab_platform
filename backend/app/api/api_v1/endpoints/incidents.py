from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db import models, schemas, session
from typing import List

router = APIRouter()

# Use consistent AsyncSession dependency
get_db = session.get_db

@router.get("/incidents/", response_model=List[schemas.Incident])
async def get_all_incidents(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Incident))
    incidents = result.scalars().all()
    return incidents

@router.post("/incidents/", response_model=schemas.Incident)
async def create_incident(incident: schemas.IncidentCreate, db: AsyncSession = Depends(get_db)):
    db_incident = models.Incident(**incident.dict())
    db.add(db_incident)
    await db.commit()
    await db.refresh(db_incident)
    return db_incident

@router.put("/incidents/{incident_id}", response_model=schemas.Incident)
async def update_incident(
    incident_id: int,
    updated: schemas.IncidentCreate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(models.Incident).where(models.Incident.id == incident_id))
    incident = result.scalars().first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    for key, value in updated.dict().items():
        setattr(incident, key, value)
    await db.commit()
    await db.refresh(incident)
    return incident

@router.delete("/incidents/{incident_id}")
async def delete_incident(incident_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Incident).where(models.Incident.id == incident_id))
    incident = result.scalars().first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    await db.delete(incident)
    await db.commit()
    return {"message": "Incident deleted"}
