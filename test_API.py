from fastapi.testclient import TestClient
from Moise_API import app

client = TestClient(app)


def test_read_predict_positive():
    response = client.post("/predict/", json={"text": "Я люблю машинное обучение"})
    assert response.status_code == 200
    response_data = response.json()
    assert response_data[0]["label"] == "positive"


def test_read_predict_negative():
    response = client.post("/predict/", json={"text": "Я ненавижу запад"})
    assert response.status_code == 200
    response_data = response.json()
    assert response_data[0]["label"] == "negative"
