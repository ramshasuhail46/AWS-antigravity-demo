from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_calculate_total():
    response = client.post(
        "/calculate-total",
        json={"item": "coffee", "amount": 10.0, "tax_rate": 5.0}
    )
    assert response.status_code == 200
    assert response.json() == {"item": "coffee", "total": 10.50}

def test_calculate_total_precision():
    response = client.post(
        "/calculate-total",
        json={"item": "book", "amount": 10.123, "tax_rate": 5.0}
    )
    assert response.status_code == 200
    assert response.json() == {"item": "book", "total": 10.63}
