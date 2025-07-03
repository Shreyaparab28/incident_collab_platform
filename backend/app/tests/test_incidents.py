import pytest
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport
from app.main import app

transport = ASGITransport(app=app)

@pytest.mark.asyncio
async def test_create_and_read_incident():
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Create
        response = await ac.post("/incidents/", json={
            "title": "Power Outage",
            "description": "Transformer failure near Main Street",
            "status": "open"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Power Outage"
        incident_id = data["id"]

        # Read
        print("POST response:", data)
	response = await ac.get(f"/incidents/{incident_id}")
        assert response.status_code == 200
        assert response.json()["title"] == "Power Outage"

        # Update
        response = await ac.put(f"/incidents/{incident_id}", json={
            "title": "Power Outage Updated",
            "description": "Updated description",
            "status": "resolved"
        })
        assert response.status_code == 200
        assert response.json()["status"] == "resolved"

        # Delete
        response = await ac.delete(f"/incidents/{incident_id}")
        assert response.status_code == 200

        # Verify Deletion
        response = await ac.get(f"/incidents/{incident_id}")
        assert response.status_code == 404
