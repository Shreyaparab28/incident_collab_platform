# app/utils/realtime.py

import redis.asyncio as redis
import json

r = redis.Redis(host="redis", port=6379)

async def publish_incident_event(action: str, data: dict):
    """Publish a message to the 'incidents' channel for websocket auto-refresh."""
    message = json.dumps({"action": action, "data": data})
    await r.publish("incidents", message)
