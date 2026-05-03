from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_calculate_total_success():
    response = client.post(
        "/calculate-total",
        json={"item": "Laptop", "amount": 1000, "tax_rate": 10}
    )
    assert response.status_code == 200
    assert response.json() == {"item": "Laptop", "total": 1100.0}

def test_calculate_total_zero_tax():
    response = client.post(
        "/calculate-total",
        json={"item": "Bread", "amount": 2.5, "tax_rate": 0}
    )
    assert response.status_code == 200
    assert response.json() == {"item": "Bread", "total": 2.5}

def test_calculate_total_invalid_data():
    response = client.post(
        "/calculate-total",
        json={"item": "Invalid", "amount": "not-a-number", "tax_rate": 5}
    )
    assert response.status_code == 422

def test_calculate_total_precision():
    response = client.post(
        "/calculate-total",
        json={"item": "Widget", "amount": 100.1, "tax_rate": 5}
    )
    assert response.status_code == 200
    # 100.1 + (100.1 * 0.05) = 100.1 + 5.005 = 105.105
    # Rounded to 2 decimal places: 105.11
    assert response.json()["total"] == 105.11
