from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_calculate_total():
    response = client.post(
        "/calculate-total",
        json={"item": "apple", "amount": 100.0, "tax_rate": 5.0}
    )
    assert response.status_code == 200
    assert response.json() == {"item": "apple", "total": 105.0}

def test_calculate_total_precision():
    # Testing for precision errors in float. Total should be rounded to 2 decimal places.
    # 10.12 + 10.12 * 0.035 = 10.4742 -> should round to 10.47
    response = client.post(
        "/calculate-total",
        json={"item": "banana", "amount": 10.12, "tax_rate": 3.5}
    )
    assert response.status_code == 200
    assert response.json()["total"] == 10.47
