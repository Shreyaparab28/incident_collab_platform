# app/websocket.py

from fastapi import APIRouter, WebSocket
import redis.asyncio as redis
import json

r = redis.Redis(host="redis", port=6379)

async def notify_clients(action: str, data: dict):
    """Publish a message to the incidents channel for real-time updates."""
    message = json.dumps({"action": action, "data": data})
    await r.publish("incidents", message)

router = APIRouter()

@router.websocket("/ws/incidents")  # ✅ Missing decorator added
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    pubsub = r.pubsub()
    await pubsub.subscribe("incidents")

    try:
        async for message in pubsub.listen():
            if message["type"] == "message":
                await websocket.send_text(message["data"].decode())
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await pubsub.unsubscribe("incidents")
        # Check if close is coroutine in your redis-py version
        try:
            await pubsub.close()
        except TypeError:
            pubsub.close()  # fallback for non-async close
