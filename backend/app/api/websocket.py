from fastapi import APIRouter, WebSocket
from app.services.websocket_manager import WebSocketManager

router = APIRouter()
manager = WebSocketManager()

@router.websocket("/ws/incidents")
async def incident_socket(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(data)
    except:
        manager.disconnect(websocket)
