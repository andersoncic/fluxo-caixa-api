import pytest
from fastapi.testclient import TestClient
from main import app  # Certifique-se de que "main" é o nome correto do arquivo principal do projeto

client = TestClient(app)

def test_create_transaction():
    # Teste para criar uma transação
    response = client.post(
        "/transactions",
        json={
            "date": "2024-12-01",
            "type": "credit",
            "amount": 100.0
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["id"] is not None
    assert data["date"] == "2024-12-01"
    assert data["type"] == "credit"
    assert data["amount"] == 100.0

def test_create_transaction_invalid_type():
    # Teste para criar uma transação com tipo inválido
    response = client.post(
        "/transactions",
        json={
            "date": "2024-12-01",
            "type": "invalid_type",
            "amount": 100.0
        }
    )
    assert response.status_code == 422

def test_get_transactions():
    # Teste para listar todas as transações
    response = client.get("/transactions")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "id" in data[0]
        assert "date" in data[0]
        assert "type" in data[0]
        assert "amount" in data[0]
