from fastapi import WebSocket, APIRouter
import redis.asyncio as redis
import json

router = APIRouter()

r = redis.Redis(host="redis", port=6379)

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    pubsub = r.pubsub()
    await pubsub.subscribe("incidents")

    async for message in pubsub.listen():
        if message["type"] == "message":
            data = json.loads(message["data"])
            await websocket.send_json(data)
