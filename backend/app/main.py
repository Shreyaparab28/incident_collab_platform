from fastapi import FastAPI
from fastapi import WebSocket
from app.db.session import engine, Base
from app.api.api_v1 import endpoints
from app.api.api_v1.endpoints import incidents
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from app.api.api_v1.endpoints import router as api_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# CORS (for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(incidents.router, prefix="/incidents", tags=["Incidents"])
app.include_router(api_router)
app.include_router(endpoints.router)

@app.websocket("/ws/incidents")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Received: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")
