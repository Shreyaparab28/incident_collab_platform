from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from app.api.api_v1.endpoints import incidents
from app.websocket import router as websocket_router

app = FastAPI(
    title="🚀 Real-Time Incident Collaboration Platform API",
    version="0.1.0",
    description="API for managing incidents with real-time collaboration using FastAPI, PostgreSQL, Redis, and WebSockets."
)

@app.get("/")
def read_root():
    return {"message": "🚀 Real-Time Incident Collaboration Platform API is running."}

@app.on_event("startup")
async def startup_event():
    print("🚀 API startup complete. Ensure Alembic migrations are applied before starting.")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include incidents API routes
app.include_router(
    incidents.router,
    prefix="/incidents",
    tags=["incidents"],
)

# ✅ Include the websocket router separately
app.include_router(websocket_router)

# ✅ If you want a test WebSocket echo endpoint, keep this, else remove
@app.websocket("/ws/echo")
async def websocket_echo(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Received: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")
