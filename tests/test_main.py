from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_calculate_total():
    payload = {
        "item": "Test Item",
        "amount": 100.0,
        "tax_rate": 10.0
    }
    response = client.post("/calculate-total", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["item"] == "Test Item"
    # Expected: 100 + (100 * 0.1) = 110
    assert data["total"] == 110.0
