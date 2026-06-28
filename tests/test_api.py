import pytest
from fastapi.testclient import TestClient
from app.api.server import create_app
from app.config import settings

@pytest.fixture
def client():
    app = create_app()
    return TestClient(app)

def test_get_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "UP"}

def test_get_identity(client):
    response = client.get("/identity")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "email" in data
    assert data["name"] == settings.USER_NAME
    assert data["email"] == settings.USER_EMAIL

def test_get_identity_name(client):
    response = client.get("/identity/name")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert data["name"] == settings.USER_NAME

def test_get_identity_email(client):
    response = client.get("/identity/email")
    assert response.status_code == 200
    data = response.json()
    assert "email" in data
    assert data["email"] == settings.USER_EMAIL
