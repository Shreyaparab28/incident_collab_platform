from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db import models, schemas, session as db_session
from app.utils.realtime import publish_incident_event
from app.utils.auth import get_current_user

router = APIRouter()

async def get_db():
    async with db_session.async_session() as session:
        yield session

@router.get("/", response_model=list[schemas.IncidentResponse])
async def read_incidents(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Incident))
    incidents = result.scalars().all()
    return [schemas.IncidentResponse.model_validate(incident, from_attributes=True) for incident in incidents]

@router.post("/", response_model=schemas.IncidentResponse)
async def create_incident(
    incident: schemas.IncidentCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    db_incident = models.Incident(
        title=incident.title,
        description=incident.description,
        status=incident.status,
        created_by=current_user["username"],  # <= capture username here
    )
    db.add(db_incident)
    await db.commit()
    await db.refresh(db_incident)

    await publish_incident_event("create", {
        "id": db_incident.id,
        "title": db_incident.title,
        "description": db_incident.description,
        "status": db_incident.status,
        "created_at": db_incident.created_at.isoformat(),
        "created_by": db_incident.created_by,
    })
    return db_incident

@router.put("/{incident_id}", response_model=schemas.IncidentResponse)
async def update_incident(
    incident_id: int,
    incident_in: schemas.IncidentCreate,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    result = await db.execute(select(models.Incident).where(models.Incident.id == incident_id))
    incident = result.scalars().first()
    if not incident:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incident not found")

    incident.title = incident_in.title
    incident.description = incident_in.description
    incident.status = incident_in.status

    await db.commit()
    await db.refresh(incident)

    await publish_incident_event("update", {
        "id": incident.id,
        "title": incident.title,
        "description": incident.description,
        "status": incident.status,
        "created_at": incident.created_at.isoformat(),
        "created_by": incident.created_by,
    })
    return schemas.IncidentResponse.model_validate(incident, from_attributes=True)

@router.delete("/{incident_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_incident(
    incident_id: int,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    result = await db.execute(select(models.Incident).where(models.Incident.id == incident_id))
    incident = result.scalars().first()
    if not incident:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incident not found")
    await db.delete(incident)
    await db.commit()
    await publish_incident_event("deleted", {"id": incident_id})
