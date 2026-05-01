from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_calculate_total():
    response = client.post(
        "/calculate-total",
        json={"item": "Notebook", "amount": 10.0, "tax_rate": 5.0}
    )
    assert response.status_code == 200
    assert response.json() == {"item": "Notebook", "total": 10.5}

def test_calculate_total_float_precision():
    response = client.post(
        "/calculate-total",
        json={"item": "Pen", "amount": 10.15, "tax_rate": 6.8}
    )
    assert response.status_code == 200
    assert response.json() == {"item": "Pen", "total": 10.84} # Note 10.15 * 1.068 = 10.8402
