from fastapi.testclient import TestClient
from Moise_API import app

client = TestClient(app)


def test_read_predict_positive():
    response = client.post("/predict/", json={"text": "Я люблю машинное обучение"})
    assert response.status_code == 200
    response_data = response.json()
    assert "neutral" in [label["label"] for label in response_data]


def test_read_predict_negative():
    response = client.post("/predict/", json={"text": "Я ненавижу запад"})
    assert response.status_code == 200
    response_data = response.json()
    assert "neutral" in [label["label"] for label in response_data]


def test_read_predict_negative():
    response = client.post("/predict/", json={"text": "Я не хочу жить в США или в Европе"})
    assert response.status_code == 200
    response_data = response.json()
    assert "neutral" in [label["label"] for label in response_data]


def test_read_predict_negative():
    response = client.post("/predict/", json={"text": "Нужно найти решение этой проблемы"})
    assert response.status_code == 200
    response_data = response.json()
    assert "neutral" in [label["label"] for label in response_data]
