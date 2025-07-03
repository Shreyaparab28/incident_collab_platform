from fastapi import APIRouter

router = APIRouter()

def include_routes():
    from . import incidents
    router.include_router(incidents.router, prefix="/incidents", tags=["incidents"])


