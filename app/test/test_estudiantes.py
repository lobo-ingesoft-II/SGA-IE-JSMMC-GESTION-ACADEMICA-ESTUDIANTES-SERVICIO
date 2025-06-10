from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_estudiante():
    response = client.post("/estudiantes/", json={
        "nombres": "Juan",
        "apellidos": "Pérez",
        "fecha_nacimiento": "2010-05-15",
        "grado": "Primero"
    })
    assert response.status_code == 200
    assert response.json()["nombres"] == "Juan"

def test_get_estudiante():
    response = client.get("/estudiantes/1")
    assert response.status_code == 200
    assert "nombres" in response.json()

def test_list_estudiantes():
    response = client.get("/estudiantes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)