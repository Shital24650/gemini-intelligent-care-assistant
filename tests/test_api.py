from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    res = client.get("/")
    assert res.status_code == 200
    assert "AI Care Assistant" in res.text


def test_analyze_success():
    res = client.post("/analyze", json={
        "device_id": "101",
        "activity": "no_movement",
        "duration": 150,
        "heart_rate": 75,
        "location": "home"
    })

    assert res.status_code == 200

    data = res.json()

    # Check keys
    assert "device_id" in data
    assert "alert_level" in data
    assert "insight" in data

    # Check alert logic
    assert data["alert_level"] in ["NORMAL", "MEDIUM_ALERT", "HIGH_ALERT"]


def test_analyze_edge_case():
    # borderline case
    res = client.post("/analyze", json={
        "device_id": "102",
        "activity": "no_movement",
        "duration": 120,
        "heart_rate": 72,
        "location": "home"
    })

    assert res.status_code == 200

    data = res.json()
    assert data["alert_level"] in ["NORMAL", "MEDIUM_ALERT"]


def test_invalid_input():
    res = client.post("/analyze", json={
        "device_id": "103",
        "activity": "no_movement",
        "duration": "invalid"   # ❌ wrong type
    })

    assert res.status_code == 422
