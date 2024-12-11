import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_daily_summary():
    # Insere dados para o teste
    client.post(
        "/transactions",
        json={
            "date": "2024-12-01",
            "type": "credit",
            "amount": 150.0
        }
    )
    client.post(
        "/transactions",
        json={
            "date": "2024-12-01",
            "type": "debit",
            "amount": 50.0
        }
    )
    
    # Testa o resumo diário
    response = client.get("/summary?date=2024-12-01")
    assert response.status_code == 200
    data = response.json()
    assert data["date"] == "2024-12-01"
    assert data["total_credit"] == 150.0
    assert data["total_debit"] == 50.0
    assert data["balance"] == 100.0

def test_summary_no_data():
    # Testa o resumo diário para uma data sem lançamentos
    response = client.get("/summary?date=2024-12-02")
    assert response.status_code == 200
    data = response.json()
    assert data["date"] == "2024-12-02"
    assert data["total_credit"] == 0.0
    assert data["total_debit"] == 0.0
    assert data["balance"] == 0.0
