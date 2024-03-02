from fastapi.testclient import TestClient
from Moise_API import app

client = TestClient(app)


def test_read_predict_positive():
    response = client.post("/predict/",
                           json=["text", "Я люблю машинное обучение"]
                           )
    json_data = response.json()

    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_read_predict_negative():
    response = client.post("/predict/",
                           json=["text", "Я ненавижу запад"]
                           )
    json_data = response.json()

    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'
