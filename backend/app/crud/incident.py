from sqlalchemy.orm import Session
from app.models.incident import Incident
from app.schemas.incident import IncidentCreate
import redis
import json

r=redis.Redis(host="redis",port=6379)

def create_incident(db: Session, incident: IncidentCreate):
    db_incident = Incident(
        title=incident.title,
        description=incident.description,
        status=incident.status
    )
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
     r.publish("incidents", json.dumps({
        "event": "new_incident",
        "data": {
            "id": db_incident.id,
            "title": db_incident.title,
            "description": db_incident.description
        }
    }))
    return db_incident
    

def get(db: Session, id: int):
    return get_incident(db, id)


def get_incident(db: Session, incident_id: int):
    return db.query(Incident).filter(Incident.id == incident_id).first()

def get_incidents(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Incident).offset(skip).limit(limit).all()
