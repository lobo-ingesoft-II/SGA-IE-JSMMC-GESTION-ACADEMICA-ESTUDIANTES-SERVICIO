from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_estudiante():
    response = client.post("/estudiantes/", json={
        "id_usuario": 1,
        "id_acudiente": 2,
        "fecha_nacimiento": "2010-05-10",
        "id_curso": 3,
        "estado_matricula": "matriculado",
        "sede": "Principal"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["id_usuario"] == 1
    assert data["estado_matricula"] == "matriculado"