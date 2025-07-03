from fastapi import APIRouter
from app.api.api_v1.endpoints import incidents

api_router = APIRouter()
api_router.include_router(incidents.router, prefix="/incidents", tags=["incidents"])
