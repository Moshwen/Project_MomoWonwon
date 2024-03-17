from fastapi.testclient import TestClient
from Moise_API import app

client = TestClient(app)


def test_read_predict_positive():
    response = client.post("/predict/", json={"text": "Я люблю машинное обучение"})
    assert response.status_code == 200
    assert response.json() == {"label": "0.95"}


def test_read_predict_negative():
    response = client.post("/predict/", json={"text": "Я ненавижу запад"})
    assert response.status_code == 200
    assert response.json() == {"label": "0.95"}
